import os
import json
import hashlib
import pickle
import asyncio
import sqlite3
import tempfile
from functools import lru_cache
from typing import Optional

from fastapi import FastAPI, Request, HTTPException, UploadFile, File
from fastapi.responses import HTMLResponse, FileResponse, StreamingResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import edge_tts
import httpx

# AI Imports
import google.generativeai as genai
from dotenv import load_dotenv

from reader3 import Book, BookMetadata, ChapterContent, TOCEntry, process_epub, save_to_pickle

# Load .env file automatically
load_dotenv()

# Configure Gemini
GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")

if GOOGLE_API_KEY:
    genai.configure(api_key=GOOGLE_API_KEY)
    # Applying vercel-best-practice: Using gemini-3-flash-preview for speed/cost balance,
    # but the prompt engineering ensures Pro-level depth.
    model = genai.GenerativeModel('gemini-3-flash-preview')
else:
    print("Warning: Neither GEMINI_API_KEY nor GOOGLE_API_KEY found in environment.")
    model = None

# Google Translate direct API (fast, connection-pooled)
_gt_client = httpx.AsyncClient(timeout=5, http2=False)

def _detect_cjk_ratio(text):
    cjk = sum(1 for c in text if '\u4e00' <= c <= '\u9fff' or '\u3040' <= c <= '\u30ff' or '\uac00' <= c <= '\ud7af')
    return cjk / max(len(text), 1)

async def _google_translate(text, dest='zh-CN'):
    """Direct Google Translate API call, ~100ms with connection reuse."""
    resp = await _gt_client.get('https://translate.googleapis.com/translate_a/single', params={
        'client': 'gtx', 'sl': 'auto', 'tl': dest, 'dt': 't', 'q': text
    })
    data = resp.json()
    return ''.join(s[0] for s in data[0] if s[0])

# ECDICT offline dictionary (~3.4M entries, <1ms lookup)
_dict_db_path = os.path.join(os.path.dirname(__file__), 'dict', 'stardict.db')
_dict_conn = None
if os.path.exists(_dict_db_path):
    _dict_conn = sqlite3.connect(_dict_db_path, check_same_thread=False)
    _dict_conn.row_factory = sqlite3.Row

def _dict_lookup(word: str) -> dict | None:
    """Look up a word in the local ECDICT dictionary. Returns dict or None."""
    if not _dict_conn:
        return None
    row = _dict_conn.execute(
        'SELECT word, phonetic, translation, definition FROM stardict WHERE word = ? COLLATE NOCASE',
        (word.strip(),)
    ).fetchone()
    if not row or not (row['translation'] or row['definition']):
        return None
    return {
        'word': row['word'],
        'phonetic': row['phonetic'] or '',
        'translation': (row['translation'] or '').strip(),
        'definition': (row['definition'] or '').strip(),
    }

async def _wiki_summary(term: str) -> dict:
    """Fetch Wikipedia summary for a term. Auto-detect language."""
    import urllib.request, urllib.parse
    is_cjk = _detect_cjk_ratio(term) > 0.3
    lang = 'zh' if is_cjk else 'en'
    try:
        encoded = urllib.parse.quote(term)
        url = f'https://{lang}.wikipedia.org/api/rest_v1/page/summary/{encoded}'
        req = urllib.request.Request(url, headers={'User-Agent': 'Reader3/1.0'})
        def _fetch():
            with urllib.request.urlopen(req, timeout=5) as resp:
                return json.loads(resp.read())
        data = await asyncio.to_thread(_fetch)
        return {
            'title': data.get('title', ''),
            'extract': data.get('extract', ''),
            'url': data.get('content_urls', {}).get('desktop', {}).get('page', ''),
        }
    except Exception:
        return {}

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Where are the book folders located?
BOOKS_DIR = "."

# TTS audio cache directory
TTS_CACHE_DIR = os.path.join(BOOKS_DIR, ".tts_cache")
os.makedirs(TTS_CACHE_DIR, exist_ok=True)

# server-cache-lru: Multi-level cache for AI Analysis
# We use both in-memory and could easily extend to disk.
_analysis_cache = {}

def _get_text_hash(text: str) -> str:
    return hashlib.md5(text.encode()).hexdigest()

@lru_cache(maxsize=20)
def load_book_cached(folder_name: str) -> Optional[Book]:
    """Load a Book object from its pickle file, with LRU caching."""
    file_path = os.path.join(BOOKS_DIR, folder_name, "book.pkl")
    if not os.path.exists(file_path):
        return None
    try:
        with open(file_path, "rb") as f:
            return pickle.load(f)
    except Exception:
        return None

@app.get("/", response_class=HTMLResponse)
async def library_view(request: Request):
    books = []
    if os.path.exists(BOOKS_DIR):
        for item in sorted(os.listdir(BOOKS_DIR)):
            if item.endswith("_data") and os.path.isdir(item):
                book = load_book_cached(item)
                if book:
                    books.append({
                        "id": item,
                        "title": book.metadata.title,
                        "author": ", ".join(book.metadata.authors),
                        "chapters": len(book.spine),
                        "language": book.metadata.language or "en",
                    })
    return templates.TemplateResponse("library.html", {"request": request, "books": books})


def _find_cover_image(book_id: str) -> str | None:
    """Find cover image path for a book. Returns absolute path or None."""
    import re
    images_dir = os.path.join(BOOKS_DIR, book_id, "images")
    if not os.path.isdir(images_dir):
        return None
    # 1. Look for files named cover*
    for f in os.listdir(images_dir):
        if re.match(r'cover', f, re.I) and f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
            return os.path.join(images_dir, f)
    # 2. Look for *_cover* pattern
    for f in os.listdir(images_dir):
        if 'cover' in f.lower() and f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
            return os.path.join(images_dir, f)
    # 3. Parse first chapter HTML for image reference
    book = load_book_cached(book_id)
    if book and book.spine:
        content = book.spine[0].content[:1000]
        m = re.search(r'(?:src|href)=["\']([^"\']+\.(?:jpe?g|png|gif))', content, re.I)
        if m:
            src = m.group(1)
            fname = os.path.basename(src)
            path = os.path.join(images_dir, fname)
            if os.path.exists(path):
                return path
    return None


@app.get("/api/book-cover/{book_id}")
async def serve_book_cover(book_id: str):
    """Serve cover image for an imported book."""
    safe_id = os.path.basename(book_id)
    cover = _find_cover_image(safe_id)
    if cover and os.path.exists(cover):
        return FileResponse(cover)
    raise HTTPException(status_code=404, detail="No cover found")

@app.get("/read/{book_id}/{chapter_index}", response_class=HTMLResponse)
async def read_chapter(request: Request, book_id: str, chapter_index: str):
    """Render a single chapter, or serve an image if chapter_index is a filename."""
    # Handle ../images/ or ../Images/ relative paths (book_id would be "images" or "Images")
    if book_id.lower() == 'images':
        referer = request.headers.get("referer", "")
        import re as _re
        from urllib.parse import unquote
        m = _re.search(r'/read/([^/]+)/', referer)
        if m:
            real_book_id = unquote(m.group(1))
            safe_name = os.path.basename(chapter_index)
            image_path = os.path.join(BOOKS_DIR, real_book_id, "images", safe_name)
            if os.path.exists(image_path):
                return FileResponse(image_path)
        raise HTTPException(status_code=404, detail="Image not found")

    # If it looks like a file (has extension), serve as image fallback
    if '.' in chapter_index:
        safe_name = os.path.basename(chapter_index)
        image_path = os.path.join(BOOKS_DIR, book_id, "images", safe_name)
        if os.path.exists(image_path):
            return FileResponse(image_path)
        raise HTTPException(status_code=404, detail="Not found")

    try:
        idx = int(chapter_index)
    except ValueError:
        raise HTTPException(status_code=404, detail="Not found")

    book = load_book_cached(book_id)
    if not book or idx < 0 or idx >= len(book.spine):
        raise HTTPException(status_code=404, detail="Not found")

    current_chapter = book.spine[idx]
    prev_idx = idx - 1 if idx > 0 else None
    next_idx = idx + 1 if idx < len(book.spine) - 1 else None

    # Fix SVG cover distortion: replace preserveAspectRatio="none" and width/height="100%"
    import re as _re
    content = current_chapter.content
    if '<svg' in content:
        content = _re.sub(r'preserveaspectratio="none"', 'preserveAspectRatio="xMidYMid meet"', content, flags=_re.I)
        content = _re.sub(r'(<svg[^>]*)\s+width="100%"', r'\1', content, flags=_re.I)
        content = _re.sub(r'(<svg[^>]*)\s+height="100%"', r'\1', content, flags=_re.I)

    return templates.TemplateResponse("reader.html", {
        "request": request, "book": book, "current_chapter": current_chapter,
        "chapter_index": idx, "book_id": book_id,
        "prev_idx": prev_idx, "next_idx": next_idx,
        "chapter_content": content
    })


@app.get("/read/{book_id}/images/{image_name}")
async def serve_book_image(book_id: str, image_name: str):
    """Serve an image file from a book's extracted images directory."""
    safe_name = os.path.basename(image_name)
    image_path = os.path.join(BOOKS_DIR, book_id, "images", safe_name)
    if not os.path.exists(image_path):
        raise HTTPException(status_code=404, detail="Image not found")
    return FileResponse(image_path)


# --- Delete books ---
@app.post("/api/delete-books")
async def delete_books(req: dict):
    """Delete one or more books by their IDs."""
    import shutil
    book_ids = req.get("book_ids", [])
    if not book_ids:
        raise HTTPException(status_code=400, detail="No books specified")
    deleted = []
    for bid in book_ids:
        safe_id = os.path.basename(bid)
        book_dir = os.path.join(BOOKS_DIR, safe_id)
        if os.path.isdir(book_dir) and os.path.exists(os.path.join(book_dir, "book.pkl")):
            await asyncio.to_thread(shutil.rmtree, book_dir)
            deleted.append(safe_id)
    load_book_cached.cache_clear()
    return {"deleted": deleted, "count": len(deleted)}

# --- AI MODULE REFACTORED (Gemini 3 Pro standards) ---

class AIAnalyzeRequest(BaseModel):
    book_id: str
    chapter_index: int

@app.post("/api/ai/analyze")
async def analyze_chapter(req: AIAnalyzeRequest):
    """Analyze a chapter using Gemini and return structured insights."""
    if not model:
        raise HTTPException(status_code=500, detail="AI not configured")

    book = load_book_cached(req.book_id)
    if not book or req.chapter_index < 0 or req.chapter_index >= len(book.spine):
        raise HTTPException(status_code=404, detail="Chapter not found")
    chapter = book.spine[req.chapter_index]

    # Use text field, fallback to stripping HTML from content
    chapter_text = chapter.text.strip()
    if not chapter_text and chapter.content:
        from html.parser import HTMLParser
        class _Strip(HTMLParser):
            def __init__(self):
                super().__init__()
                self.parts = []
            def handle_data(self, d):
                self.parts.append(d)
        s = _Strip()
        s.feed(chapter.content)
        chapter_text = ' '.join(s.parts).strip()

    if len(chapter_text) < 20:
        return {
            "summary": "本章内容过短，无法进行有效分析。",
            "key_points": [],
            "difficulties": "",
            "insight": ""
        }

    # server-cache-lru: Fingerprint based on text content hash
    content_hash = _get_text_hash(chapter_text)
    cache_key = f"{req.book_id}:{req.chapter_index}:{content_hash}"

    if cache_key in _analysis_cache:
        return _analysis_cache[cache_key]

    prompt = f"""
    你是一位精通文学分析与叙事学的资深教授。请对以下文本进行【多维深度解构】。

    书名：{book.metadata.title}
    章节：{chapter.title}

    【待分析文本】：
    {chapter_text[:15000]} 

    请严格按照以下 JSON 结构返回分析结果（禁止包含任何 Markdown 标记如 ```json）：

    {{
        "summary": "一段约200字的叙事学总结，分析本章的情绪曲线和叙事功能。",
        "key_points": [
            "关键冲突或伏笔1",
            "关键冲突或伏笔2",
            "..."
        ],
        "difficulties": "解析本章中的文化隐喻、复杂修辞或生僻词汇。",
        "insight": "提供一个独特的视角，探讨本章背后的哲学命题或时代背景。"
    }}
    """

    try:
        # Use asyncio.to_thread to keep FastAPI loop responsive
        response = await asyncio.to_thread(model.generate_content, prompt)
        text = response.text.strip()
        
        # Robust JSON cleaning
        if "{" in text and "}" in text:
            text = text[text.find("{"):text.rfind("}")+1]
            
        result = json.loads(text)
        _analysis_cache[cache_key] = result # Cache the processed object
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")

@app.post("/api/ai/translate")
async def translate_text(req: dict):
    """Translate text using Gemini."""
    if not model:
        raise HTTPException(status_code=500, detail="AI not configured")
    text = req.get("text", "")
    if not text:
        return {"translation": ""}

    prompt = f"""你是一位享誉国际的翻译家，追求“信、达、雅”。请将以下文本翻译成中文。
    如果是小说，请保留叙事风格；如果是诗歌，请保留韵律；如果是专业文档，请确保术语准确。
    只返回译文内容。
    
    原文：
    {text}"""
    
    try:
        response = await asyncio.to_thread(model.generate_content, prompt)
        return {"translation": response.text.strip()}
    except Exception as e:
        return {"translation": f"[Translation Error: {str(e)}]"}


@app.post("/api/ai/translate-stream")
async def translate_text_stream(req: dict):
    """Translate text using Gemini with streaming output, auto-detect language direction."""
    if not model:
        raise HTTPException(status_code=500, detail="AI not configured")
    text = req.get("text", "")
    if not text:
        return StreamingResponse(iter([""]), media_type="text/plain")

    # Auto-detect: if mostly CJK → translate to English, otherwise → translate to Chinese
    cjk_count = sum(1 for c in text if '\u4e00' <= c <= '\u9fff' or '\u3040' <= c <= '\u30ff' or '\uac00' <= c <= '\ud7af')
    if cjk_count > len(text) * 0.3:
        target = "英文"
    else:
        target = "中文"

    prompt = f"""你是一位享誉国际的翻译家，追求"信、达、雅"。请将以下文本翻译成{target}。
如果是小说，请保留叙事风格；如果是诗歌，请保留韵律；如果是专业文档，请确保术语准确。
只返回译文内容，不要任何解释。

原文：
{text}"""

    def generate():
        try:
            response = model.generate_content(prompt, stream=True)
            for chunk in response:
                try:
                    if chunk.text:
                        yield chunk.text
                except (ValueError, AttributeError):
                    continue
        except Exception as e:
            yield f"[Translation Error: {str(e)}]"

    return StreamingResponse(generate(), media_type="text/plain; charset=utf-8")


@app.post("/api/quick-translate")
async def quick_translate(req: dict):
    """Dict lookup (instant) → Google Translate fallback (~100ms)."""
    text = (req.get("text") or "").strip()
    if not text:
        return {"translation": ""}

    # Step 1: Try local dictionary for single words/short phrases
    dict_result = _dict_lookup(text)
    if dict_result:
        return {
            "source": "dict",
            "word": dict_result['word'],
            "phonetic": dict_result['phonetic'],
            "translation": dict_result['translation'],
            "definition": dict_result['definition'],
        }

    # Step 2: Fallback to Google Translate
    is_cjk = _detect_cjk_ratio(text) > 0.3
    dest = 'en' if is_cjk else 'zh-CN'
    try:
        translation = await _google_translate(text, dest)
        return {"source": "google", "translation": translation}
    except Exception as e:
        return {"source": "error", "translation": "", "error": str(e)}


@app.post("/api/wiki-lookup")
async def wiki_lookup(req: dict):
    """Wikipedia summary for a term."""
    text = (req.get("text") or "").strip()
    if not text:
        return {"extract": ""}
    result = await _wiki_summary(text)
    return result


class AIChatRequest(BaseModel):
    book_id: str
    chapter_index: int
    question: str


@app.post("/api/ai/chat")
async def chat_about_chapter(req: AIChatRequest):
    """Answer a free-form question about the current chapter."""
    if not model:
        raise HTTPException(status_code=500, detail="AI not configured")

    book = load_book_cached(req.book_id)
    if not book or req.chapter_index < 0 or req.chapter_index >= len(book.spine):
        raise HTTPException(status_code=404, detail="Chapter not found")
    chapter = book.spine[req.chapter_index]

    # Use text field, fallback to stripping HTML from content
    chapter_text = chapter.text.strip()
    if not chapter_text and chapter.content:
        from html.parser import HTMLParser
        class _Strip(HTMLParser):
            def __init__(self):
                super().__init__()
                self.parts = []
            def handle_data(self, d):
                self.parts.append(d)
        s = _Strip()
        s.feed(chapter.content)
        chapter_text = ' '.join(s.parts).strip()

    prompt = f"""你是一位博学的阅读助手。基于以下书籍章节内容，回答用户的问题。
如果问题与章节内容无关，也可以根据你的知识回答，但请注明这不在当前章节中。
回答请简洁明了，使用与用户提问相同的语言。

书名：{book.metadata.title}
章节：{chapter.title}

【章节内容】：
{chapter_text[:12000]}

【用户提问】：
{req.question}"""

    try:
        response = await asyncio.to_thread(model.generate_content, prompt)
        return {"answer": response.text.strip()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Chat failed: {str(e)}")


# --- TTS MODULE: edge-tts (local, free, low latency) ---

@app.get("/api/tts")
async def stream_tts(text: str, voice: str = "zh-CN-XiaoxiaoNeural", rate: str = "+0%"):
    """Stream TTS audio via edge-tts."""
    communicate = edge_tts.Communicate(text, voice, rate=rate)
    async def generate():
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                yield chunk["data"]
    return StreamingResponse(generate(), media_type="audio/mpeg")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8123)


# --- Apple Books Integration ---

APPLE_BOOKS_DB = os.path.expanduser(
    "~/Library/Containers/com.apple.iBooksX/Data/Documents/BKLibrary/BKLibrary-1-091020131601.sqlite"
)
APPLE_BOOKS_COVER_DIR = os.path.expanduser(
    "~/Library/Containers/com.apple.iBooksX/Data/Library/Caches/BCCoverCache-1/BICDiskDataStore"
)

@app.get("/api/apple-books")
async def list_apple_books():
    """List books from Apple Books library."""
    if not os.path.exists(APPLE_BOOKS_DB):
        return {"books": [], "error": "Apple Books database not found"}

    def _query():
        conn = sqlite3.connect(APPLE_BOOKS_DB)
        conn.row_factory = sqlite3.Row
        rows = conn.execute(
            "SELECT ZTITLE, ZAUTHOR, ZPATH, ZFILESIZE, ZASSETID FROM ZBKLIBRARYASSET "
            "WHERE ZTITLE IS NOT NULL AND ZPATH IS NOT NULL AND ZCONTENTTYPE = 1 "
            "ORDER BY ZTITLE"
        ).fetchall()
        conn.close()
        return [dict(r) for r in rows]

    rows = await asyncio.to_thread(_query)

    books = []
    for r in rows:
        path = r['ZPATH']
        if not path or not os.path.exists(path):
            continue
        base_name = os.path.splitext(os.path.basename(path))[0]
        book_id = base_name + "_data"
        already_imported = os.path.exists(os.path.join(BOOKS_DIR, book_id, "book.pkl"))
        books.append({
            "title": r['ZTITLE'],
            "author": r['ZAUTHOR'] or '',
            "path": path,
            "size_mb": round((r['ZFILESIZE'] or 0) / 1048576, 1),
            "imported": already_imported,
            "asset_id": r['ZASSETID'] or '',
        })
    return {"books": books}


@app.get("/api/apple-books/cover/{asset_id}")
async def serve_apple_books_cover(asset_id: str):
    """Serve a cover image from Apple Books cache."""
    import subprocess
    safe_id = os.path.basename(asset_id)
    cover_dir = os.path.join(APPLE_BOOKS_COVER_DIR, safe_id)
    if not os.path.isdir(cover_dir):
        raise HTTPException(status_code=404, detail="Cover not found")
    # Check for cached JPEG first
    jpeg_path = os.path.join(cover_dir, f"{safe_id}.jpg")
    if os.path.exists(jpeg_path) and os.path.getsize(jpeg_path) > 0:
        return FileResponse(jpeg_path, media_type="image/jpeg")
    # Find largest HEIC file (best quality)
    import glob as _glob
    heics = sorted(_glob.glob(os.path.join(cover_dir, "*.heic")), key=os.path.getsize, reverse=True)
    if not heics:
        raise HTTPException(status_code=404, detail="No cover image")
    # Convert HEIC to JPEG synchronously (awaited)
    result = await asyncio.to_thread(
        subprocess.run,
        ["sips", "-s", "format", "jpeg", heics[0], "--out", jpeg_path],
        capture_output=True, timeout=10
    )
    if os.path.exists(jpeg_path) and os.path.getsize(jpeg_path) > 0:
        return FileResponse(jpeg_path, media_type="image/jpeg")
    raise HTTPException(status_code=500, detail="Cover conversion failed")


@app.post("/api/import-local")
async def import_local_epub(req: dict):
    """Import an EPUB from a local file path (e.g. Apple Books)."""
    path = req.get("path", "")
    if not path or not os.path.exists(path):
        raise HTTPException(status_code=400, detail="File not found")
    if not path.lower().endswith('.epub'):
        raise HTTPException(status_code=400, detail="Only .epub files are supported")

    base_name = os.path.splitext(os.path.basename(path))[0]
    out_dir = os.path.join(BOOKS_DIR, base_name + "_data")

    book_obj = await asyncio.to_thread(process_epub, path, out_dir)
    await asyncio.to_thread(save_to_pickle, book_obj, out_dir)
    load_book_cached.cache_clear()

    return {
        "success": True,
        "book_id": base_name + "_data",
        "title": book_obj.metadata.title,
        "chapters": len(book_obj.spine),
    }


@app.post("/api/upload")
async def upload_epub(file: UploadFile = File(...)):
    """Upload and process an EPUB file."""
    if not file.filename or not file.filename.lower().endswith('.epub'):
        raise HTTPException(status_code=400, detail="Only .epub files are supported")

    # Save to temp file
    with tempfile.NamedTemporaryFile(suffix='.epub', delete=False) as tmp:
        content = await file.read()
        tmp.write(content)
        tmp_path = tmp.name

    try:
        # Determine output dir name
        base_name = os.path.splitext(file.filename)[0]
        out_dir = os.path.join(BOOKS_DIR, base_name + "_data")

        # Process in thread to avoid blocking
        book_obj = await asyncio.to_thread(process_epub, tmp_path, out_dir)
        await asyncio.to_thread(save_to_pickle, book_obj, out_dir)

        # Clear LRU cache so new book appears
        load_book_cached.cache_clear()

        return {
            "success": True,
            "book_id": base_name + "_data",
            "title": book_obj.metadata.title,
            "chapters": len(book_obj.spine),
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to process EPUB: {str(e)}")
    finally:
        os.unlink(tmp_path)
