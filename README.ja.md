[English](README.en.md) | [简体中文](README.md) | [繁體中文](README.zh-Hant.md) | 日本語 | [한국어](README.ko.md) | [Español](README.es.md) | [Français](README.fr.md) | [Italiano](README.it.md)

# 🧊 Smoothie Reader (Reader3)

> 「AIによって技術が民主化されるとき、美学と人間中心のデザインこそが究極の差別化要因となる。」

Andrej Karpathyの[ミニマリスト・リーダー・プロトタイプ](https://x.com/karpathy/status/1990577951671509438)に触発されたSmoothie Readerは、深い読書のために設計された、AI拡張型のキュレーション環境です。上海を拠点とする現代アートキュレーターとして、私は従来の「LLMへのコピペ」というワークフローを、読者、テキスト、そしてマシンの間の流動的でシームレスな対話へと進化させました。

🏛️ **初回展示：自省録**。集中した沈思の精神に敬意を表し、本リポジトリにはマルクス・アウレリウスの『自省録』（Project Gutenberg提供）があらかじめロードされています。

<div align="center">
  <img src="assets/library.jpg" width="800" alt="Library"><br>
  <sub>パーソナルライブラリを一望</sub>
</div>

## ✨ キュレーションのビジョン

多くのリーダーがテキストを表示するだけであるのに対し、Smoothie Readerはすべてのページを一つの展示物として扱い、読書を総合的な知的体験へと変容させます。

- 🔍 **直感的な発見**：テキストを選択するだけでアクションバーが表示されます。**ECDICT (英語)** および中国語のオフライン辞書を内蔵。
- 🤖 **拡張された対話**:
  - **ナラティブ翻訳**：文脈に応じた高品質な翻訳を、原文の下にエレガントに埋め込みます。
  - **デジタル・コンパニオン**：ストリーミング対話と多重文脈の記憶をサポートするサイドバーAIアシスタントが、深い知の探求を支えます。
  - **グローバルな接続性**：Gemini, OpenAI, Claude, DeepSeekなど、20以上の主要プロバイダーとシームレスに統合。

<div align="center">
  <img src="assets/reader_AItools.jpg" width="800" alt="AI Tools"><br>
  <sub>選択ツールバー · インライン翻訳 · AIコンパニオンサイドバー</sub>
</div>

- 🔊 **音の瞑想 (TTS)**：Edge-TTSを搭載し、90種類以上の高品質な音声で書かれた言葉に命を吹き込みます。
- ✏️ **アーカイブ**：5色の美的ハイライト、インライン注釈、永続的なブックマーク。データはすべて**ローカルの保管庫**に保存されます。

<div align="center">
  <img src="assets/reader_catelog.jpg" width="800" alt="Reading Layout"><br>
  <sub>3カラム閲覧：目次ナビ · 没入型テキスト · マルチカラーハイライト</sub>
</div>

- 🎨 **ミニマリズムの美学**：厳選された6つのテーマと柔軟な3カラムレイアウトにより、あらゆるデバイスで明晰な集中を。

<div align="center">
  <img src="assets/reader_setting.jpg" width="800" alt="Settings"><br>
  <sub>テーマ、タイポグラフィ、辞書、AIモデル — ワンストップ設定</sub>
</div>

## 🚀 インストール

本プロジェクトは、高速かつ隔離された実行環境を保証するため、最新の [uv](https://docs.astral.sh/uv/) を環境構築ツールとして採用しています。

### 1. 準備
Python 3.9以上がインストールされていることを確認してください。`uv` オーケストレーターをインストールします：
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. 展示の開始
```bash
# 最初の作品をインポート (例: ドラキュラ)
uv run reader3.py dracula.epub

# 環境を起動
uv run server.py
```
ブラウザでアクセス：👉 **http://localhost:8123**

### 3. AIの起動
読書インターフェースに入り、**設定 (Settings)** から **AIプロバイダー** を構成します。あなたの感性をマシンと接続してください（例：[Gemini Keyを無料で取得](https://aistudio.google.com/apikey)）。

> [!TIP]
> **🚀 秘密の通路 (裏技)**：ページ上のどこでも、儀式 **`↑ ↑ ↓ ↓ ← → ← → B A`** (コナミコマンド) を実行すると、マルチモデル運用のための **高度なAIルーティングパネル** が現れます。

## 🛡️ 主権とプライバシー
- **ローカルの主権**：AIやTTSを明示的に呼び出さない限り、データがあなたの聖域を離れることはありません。
- **アカウント不要**：アーカイブはブラウザの `localStorage` のみに保持されます。

## 📚 さらなる探求
詳細な設定手順については、[キュレーターズ・ガイド](docs/GUIDE.md) を参照してください。

## 📄 来歴
[MIT License](LICENSE)
