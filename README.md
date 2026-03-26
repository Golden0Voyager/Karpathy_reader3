[English](README.en.md) | 简体中文 | [繁體中文](README.zh-Hant.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Español](README.es.md) | [Français](README.fr.md) | [Italiano](README.it.md)

# 🧊 Smoothie Reader (Reader3)

> "当技术被 AI 民主化，审美与以人为本的设计便成了最终的护城河。"

灵感源自 Andrej Karpathy 的 [极简阅读器原型](https://x.com/karpathy/status/1990577951671509438)，Smoothie Reader 是一个为深度阅读而生的、经 AI 增强的策展式环境。作为一名常驻上海的当代艺术策展人，我将最初的"复制粘贴给大模型"工作流，进化为一场读者、文本与机器之间流动的、无缝的对话。

🏛️ **开幕展：沉思录**。为了向专注思考的精神致敬，本仓库预置了马可·奥勒留的《沉思录》（来源于 Project Gutenberg）。

<div align="center">
  <img src="assets/library.jpg" width="800" alt="Library"><br>
  <sub>个人藏书馆：封面墙一览无余</sub>
</div>

## ✨ 策展愿景

大多数阅读器只负责显示文字，而 Smoothie Reader 将每一页视为一个展位，将阅读转化为一场完整的智力体验：

- 🔍 **直觉探索**：选中文字秒开工具栏。内置支持 **ECDICT 英文词典** 和 **中文离线词典**。
- 🤖 **增强对话**：
  - **叙事级翻译**：一键获取高质量上下文翻译，优雅地内嵌于原文下方。
  - **数字伴读**：侧边栏 AI 助手支持流式输出和多轮记忆，随时进行深度的智力碰撞。
  - **全球连接**：完美支持 Gemini, OpenAI, Claude, DeepSeek 等 20+ 主流模型。

<div align="center">
  <img src="assets/reader_AItools.jpg" width="800" alt="AI Tools"><br>
  <sub>划词工具栏 · 行内翻译 · AI 伴读侧栏</sub>
</div>

- 🔊 **声音冥想 (TTS)**：基于 Edge-TTS，提供 90+ 种高质量语音，赋予文字真实的生命力。
- ✏️ **档案系统**：5 色美学高亮、行内笔记、书签，所有数据全部存储在您的**本地保险库**。

<div align="center">
  <img src="assets/reader_catelog.jpg" width="800" alt="Reading Layout"><br>
  <sub>三栏阅读：目录导航 · 沉浸正文 · 多色高亮</sub>
</div>

- 🎨 **极简审美**：6 种精选主题、灵活的三栏布局（目录/正文/AI），适配所有设备的极致视觉。

<div align="center">
  <img src="assets/reader_setting.jpg" width="800" alt="Settings"><br>
  <sub>主题、排版、词典、AI 模型 —— 一站式配置</sub>
</div>

## 🚀 部署安装

本项目强制使用现代化的 [uv](https://docs.astral.sh/uv/) 作为环境编排工具，确保极速与隔离的运行表现。

### 1. 准备工作
确保系统已安装 Python 3.9+。安装 `uv` 编排器：
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. 开启展览
```bash
# 导入您的第一件藏品 (以 Dracula 为例)
uv run reader3.py dracula.epub

# 启动环境
uv run server.py
```
然后打开浏览器访问：👉 **http://localhost:8123**

### 3. 激活 AI
进入阅读页面，点击左上角 **设置 (Settings)**，配置您的 **AI 提供商**，将您的灵性与机器相连（例如，[免费获取 Gemini Key](https://aistudio.google.com/apikey)）。

> [!TIP]
> **🚀 秘密通道 (秘籍)**：在页面任何地方，依次按下 **`↑ ↑ ↓ ↓ ← → ← → B A`** (Konami Code)，即可解锁隐藏的 **高级 AI 路由管理面板**。

## 🛡️ 主权与隐私
- **本地主权**：除了您主动触发的 AI 或 TTS 请求外，没有任何数据会离开您的避风港。
- **无需账号**：您的档案仅保存在浏览器 `localStorage` 中。

## 📚 进阶向导
详细的配置说明（如离线词典下载、多设备访问、端口修改），请参阅 [策展人指南](docs/GUIDE.md)。

## 📄 许可证
[MIT License](LICENSE)
