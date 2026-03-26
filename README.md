[English](README.en.md) | 简体中文 | [繁體中文](README.zh-Hant.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Español](README.es.md) | [Français](README.fr.md) | [Italiano](README.it.md)

# 🧊 Smoothie Reader (Reader3)

> "当技术被 AI 民主化，审美与以人为本的设计便成了最终的护城河。"

灵感源自 Andrej Karpathy 的 [极简阅读器原型](https://x.com/karpathy/status/1990577951671509438)，Smoothie Reader 是一个本地部署的 AI 智能电子书阅读器，集成划词查词、AI 翻译与对话、TTS 朗读、高亮笔记等功能，为深度阅读而生。

📖 **内置示例书籍**：仓库预置了马可·奥勒留的《沉思录》（来源于 Project Gutenberg），克隆后即可体验。

<div align="center">
  <img src="assets/library.jpg" width="800" alt="Library"><br>
  <sub>个人藏书馆：封面墙一览无余</sub>
</div>

## ✨ 核心功能

- 🔍 **直觉探索**：选中文字秒开工具栏。内置支持 **ECDICT 英文词典** 和 **中文离线词典**。
- 🤖 **增强对话**：
  - **叙事级翻译**：一键获取高质量上下文翻译，优雅地内嵌于原文下方。
  - **数字伴读**：侧边栏 AI 助手支持流式输出和多轮记忆，随时进行深度的智力碰撞。
  - **广泛兼容**：内置 OpenAI、Anthropic、Gemini、DeepSeek、Grok、阿里云百炼、火山引擎、腾讯混元、MiniMax、月之暗面、硅基流动、Cerebras、SambaNova、Groq、Mistral、DeepInfra、Together AI、OpenRouter、智谱AI、ModelScope 共 20 家 AI 服务商，并支持任意 OpenAI 兼容接口自定义接入。

<div align="center">
  <img src="assets/reader_AItools.jpg" width="800" alt="AI Tools"><br>
  <sub>划词工具栏 · 行内翻译 · AI 伴读侧栏</sub>
</div>

- 🔊 **TTS 朗读**：基于 Edge-TTS，提供中英文多种高质量语音，解放双眼。
- ✏️ **高亮笔记**：5 色高亮、行内笔记、书签，所有数据存储在浏览器**本地 localStorage** 中。

<div align="center">
  <img src="assets/reader_catelog.jpg" width="800" alt="Reading Layout"><br>
  <sub>三栏阅读：目录导航 · 沉浸正文 · 多色高亮</sub>
</div>

- 🎨 **极简审美**：6 种精选主题、灵活的三栏布局（目录/正文/AI），适配所有设备的极致视觉。

<div align="center">
  <img src="assets/reader_setting.jpg" width="800" alt="Settings"><br>
  <sub>主题、排版、词典、AI 模型 —— 一站式配置</sub>
</div>

## 🚀 快速开始

本项目使用 [uv](https://docs.astral.sh/uv/) 管理 Python 环境和依赖。

### 1. 安装 uv
确保系统已安装 Python 3.10+，然后安装 `uv`：
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. 导入电子书并启动
```bash
# 导入一本 EPUB 电子书
uv run reader3.py your_book.epub

# 启动服务
uv run server.py
```
然后打开浏览器访问：👉 **http://localhost:8123**

### 3. 配置 AI
进入阅读页面，点击左上角 **设置 (Settings)**，配置您的 **AI 提供商**和 API Key（例如，[免费获取 Gemini Key](https://aistudio.google.com/apikey)）。

> [!TIP]
> **🚀 秘密通道 (秘籍)**：在页面任何地方，依次按下 **`↑ ↑ ↓ ↓ ← → ← → B A`** (Konami Code)，即可解锁隐藏的 **高级 AI 路由管理面板**。

## 🛡️ 主权与隐私
- **本地优先**：除了您主动触发的 AI 或 TTS 请求外，没有任何数据会离开您的设备。
- **无需账号**：您的档案仅保存在浏览器 `localStorage` 中。

## 📚 进阶向导
详细的配置说明（如离线词典下载、多设备访问、端口修改），请参阅 [使用指南](docs/GUIDE.md)。

## 📄 许可证
[MIT License](LICENSE)
