[English](README.en.md) | [简体中文](README.md) | 繁體中文 | [日本語](README.ja.md) | [한국어](README.ko.md) | [Español](README.es.md) | [Français](README.fr.md) | [Italiano](README.it.md)

# 🧊 Smoothie Reader (Reader3)

> 「當技術被 AI 民主化，審美與以人為本的設計便成了最終的護城河。」

靈感源自 Andrej Karpathy 的 [極簡閱讀器原型](https://x.com/karpathy/status/1990577951671509438)，Smoothie Reader 是一個為深度閱讀而生的、經 AI 增強的策展式環境。作為一名常駐上海的當代藝術策展人，我將最初的「複製粘貼給大模型」工作流，進化為一場讀者、文本與機器之間流動的、無縫的對話。

🏛️ **開幕展：沉思錄**。為了向專注思考的精神致敬，本倉庫預置了馬可·奧勒留的《沉思錄》（來源於 Project Gutenberg）。

<div align="center">
  <img src="assets/library.jpg" width="800" alt="Library"><br>
  <sub>個人藏書館：封面牆一覽無餘</sub>
</div>

## ✨ 策展願景

大多數閱讀器只負責顯示文字，而 Smoothie Reader 將每一頁視為一個展位，將閱讀轉化為一場完整的智力體驗：

- 🔍 **直覺探索**：選中文字秒開工具欄。內置支持 **ECDICT 英文詞典** 和 **中文離線詞典**。
- 🤖 **增強對話**：
  - **敘事級翻譯**：一鍵獲取高質量上下文翻譯，優雅地內嵌於原文下方。
  - **數位伴讀**：側邊欄 AI 助手支持流式輸出和多輪記憶，隨時進行深度的智力碰撞。
  - **全球連接**：完美支持 Gemini, OpenAI, Claude, DeepSeek 等 20+ 主流模型。

<div align="center">
  <img src="assets/reader_AItools.jpg" width="800" alt="AI Tools"><br>
  <sub>劃詞工具欄 · 行內翻譯 · AI 伴讀側欄</sub>
</div>

- 🔊 **聲音冥想 (TTS)**：基於 Edge-TTS，提供 90+ 種高質量語音，賦予文字真實的生命力。
- ✏️ **檔案系統**：5 色美學高亮、行內筆記、書簽，所有數據全部存儲在您的**本地保險庫**。

<div align="center">
  <img src="assets/reader_catelog.jpg" width="800" alt="Reading Layout"><br>
  <sub>三欄閱讀：目錄導航 · 沉浸正文 · 多色高亮</sub>
</div>

- 🎨 **極簡審美**：6 種精選主題、靈活的三欄佈局（目錄/正文/AI），適配所有設備的極致視覺。

<div align="center">
  <img src="assets/reader_setting.jpg" width="800" alt="Settings"><br>
  <sub>主題、排版、詞典、AI 模型 —— 一站式配置</sub>
</div>

## 🚀 部署安裝

本項目強制使用現代化的 [uv](https://docs.astral.sh/uv/) 作為環境編排工具，確保極速與隔離的運行表現。

### 1. 準備工作
確保系統已安裝 Python 3.9+。安裝 `uv` 編排器：
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. 開啟展覽
```bash
# 導入您的第一件藏品 (以 Dracula 為例)
uv run reader3.py dracula.epub

# 啟動環境
uv run server.py
```
然後打開瀏覽器訪問：👉 **http://localhost:8123**

### 3. 激活 AI
進入閱讀頁面，點擊左上角 **設置 (Settings)**，配置您的 **AI 提供商**，將您的靈性與機器相連（例如，[免費獲取 Gemini Key](https://aistudio.google.com/apikey)）。

> [!TIP]
> **🚀 秘密通道 (秘籍)**：在頁面任何地方，依次按下 **`↑ ↑ ↓ ↓ ← → ← → B A`** (Konami Code)，即可解鎖隱藏的 **高級 AI 路由管理面板**。

## 🛡️ 主權與隱私
- **本地主權**：除了您主動觸發的 AI 或 TTS 請求外，沒有任何數據會離開您的避風港。
- **無需帳號**：您的檔案僅保存在瀏覽器 `localStorage` 中。

## 📚 進階向導
詳細的配置說明（如離線詞典下載、多設備訪問、端口修改），請參閱 [策展人指南](docs/GUIDE.md)。

## 📄 許可證
[MIT License](LICENSE)
