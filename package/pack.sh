#!/bin/bash
# 打包 Reader3 轻量发行版
# 用法: cd package && bash pack.sh
# 产出: package/reader3-release.zip

set -e
cd "$(dirname "$0")"
ROOT="$(cd .. && pwd)"

OUT="reader3-release"
rm -rf "$OUT" "$OUT.zip"
mkdir -p "$OUT/templates" "$OUT/dict" "$OUT/books" "$OUT/docs"

# 核心文件（从项目根目录拷贝）
cp "$ROOT/server.py" "$ROOT/reader3.py" "$ROOT/requirements.txt" "$OUT/"
cp setup.sh start.sh "$OUT/"
cp .env.example "$OUT/"
cp "$ROOT/templates/reader.html" "$ROOT/templates/library.html" "$OUT/templates/"

# 空目录占位说明
cp "$ROOT/dict/README.md" "$OUT/dict/"

# 生成 PDF 文档（从 docs/*.md 转换到 package/*.pdf）
echo "📄 生成 PDF 文档..."
python "$ROOT/tools/_md2pdf.py"

# 文档（md 从 docs/ 拷贝，pdf 从 package/ 拷贝）
cp "$ROOT/docs/INTRODUCTION.md" "$ROOT/docs/GUIDE.md" "$OUT/docs/"
for pdf in INTRODUCTION.pdf GUIDE.pdf; do
    [ -f "$pdf" ] && cp "$pdf" "$OUT/docs/"
done

# 示例图书（Dracula — Project Gutenberg 公共领域）
[ -f dracula.epub ] && cp dracula.epub "$OUT/books/"

# 打包
echo "📦 打包中..."
zip -r "$OUT.zip" "$OUT" -x "*.pyc" "*__pycache__*"

SIZE=$(du -sh "$OUT.zip" | cut -f1)
rm -rf "$OUT"

echo ""
echo "✅ 打包完成: $OUT.zip ($SIZE)"
echo ""
echo "使用说明："
echo "  1. 解压 reader3-release.zip"
echo "  2. 阅读 docs/GUIDE.md 了解详细安装步骤"
echo "  3. 运行: bash setup.sh"
echo "  4. 运行: bash start.sh"
echo "  5. 浏览器打开: http://localhost:8000"
echo "  6. 内置示例图书 Dracula 可直接在 books/ 目录中找到"
