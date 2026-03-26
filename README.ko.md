[English](README.en.md) | [简体中文](README.md) | [繁體中文](README.zh-Hant.md) | [日本語](README.ja.md) | 한국어 | [Español](README.es.md) | [Français](README.fr.md) | [Italiano](README.it.md)

# 🧊 Smoothie Reader (Reader3)

> "기술이 AI에 의해 민주화될 때, 미학과 인간 중심의 디자인이 궁극적인 차별점이 됩니다."

Andrej Karpathy의 [미니멀리스트 리더 프로토타입](https://x.com/karpathy/status/1990577951671509438)에서 영감을 받은 Smoothie Reader는 깊은 독서를 위해 설계된 AI 증강 큐레이션 환경입니다. 상하이를 기반으로 활동하는 현대 미술 큐레이터로서, 저는 기존의 "LLM에 복사-붙여넣기" 워크플로우를 독자, 텍스트, 그리고 기계 사이의 유동적이고 매끄러운 대화로 진화시켰습니다.

🏛️ **개막 전시: 명상록**. 집중된 명상의 정신을 기리기 위해, 이 저장소에는 마르쿠스 아우렐리우스의 "명상록"(Project Gutenberg 제공)이 사전 로드되어 있습니다.

<div align="center">
  <img src="assets/library.jpg" width="800" alt="Library"><br>
  <sub>개인 서재를 한눈에</sub>
</div>

## ✨ 큐레이션의 비전

대부분의 독서기가 텍스트를 표시하는 데 그치는 반면, Smoothie Reader는 모든 페이지를 하나의 전시물로 대하며 독서를 종합적인 지적 경험으로 변화시킵니다.

- 🔍 **직관적 탐색**: 텍스트를 선택하기만 하면 액션 바가 나타납니다. **ECDICT (영어)** 및 중국어 오프라인 사전 내장.
- 🤖 **증강된 대화**:
  - **내러티브 번역**: 문맥을 반영한 고품질 번역이 원문 아래에 우아하게 삽입됩니다.
  - **디지털 동반자**: 스트리밍 대화와 다중 문맥 기억을 지원하는 사이드바 AI 어시스턴트가 깊은 지적 몰입을 돕습니다.
  - **글로벌 연결성**: Gemini, OpenAI, Claude, DeepSeek 등 20개 이상의 주요 제공업체와 원활하게 통합됩니다.

<div align="center">
  <img src="assets/reader_AItools.jpg" width="800" alt="AI Tools"><br>
  <sub>선택 도구 모음 · 인라인 번역 · AI 동반자 사이드바</sub>
</div>

- 🔊 **소리 명상 (TTS)**: Edge-TTS를 통해 90개 이상의 목소리로 텍스트에 생명력을 불어넣습니다.
- ✏️ **아카이브**: 5가지 미학적 하이라이트, 인라인 주석, 영구 북마크. 모든 데이터는 **로컬 저장소**에 보관됩니다.

<div align="center">
  <img src="assets/reader_catelog.jpg" width="800" alt="Reading Layout"><br>
  <sub>3단 독서: 목차 탐색 · 몰입형 텍스트 · 멀티 컬러 하이라이트</sub>
</div>

- 🎨 **미니멀리즘 미학**: 엄선된 6가지 테마와 유연한 3단 레이아웃으로 모든 기기에서 명료한 집중을 제공합니다.

<div align="center">
  <img src="assets/reader_setting.jpg" width="800" alt="Settings"><br>
  <sub>테마, 타이포그래피, 사전, AI 모델 — 올인원 설정</sub>
</div>

## 🚀 설치 및 시작

이 프로젝트는 최신 [uv](https://docs.astral.sh/uv/)를 환경 구축 도구로 사용하여 빠르고 격리된 실행 환경을 보장합니다.

### 1. 준비
Python 3.9 이상이 필요합니다. `uv` 오케스트레이터를 설치하세요:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. 전시 개시
```bash
# 첫 번째 작품 가져오기 (예: 드라큘라)
uv run reader3.py dracula.epub

# 환경 실행
uv run server.py
```
브라우저에서 접속: 👉 **http://localhost:8123**

### 3. AI 활성화
독서 인터페이스에서 **설정 (Settings)**으로 이동하여 **AI 제공업체**를 구성하세요. 당신의 영감을 기계와 연결하세요 (예: [무료 Gemini 키 받기](https://aistudio.google.com/apikey)).

> [!TIP]
> **🚀 비밀 통로 (치트키)**: 페이지 어디에서나 **`↑ ↑ ↓ ↓ ← → ← → B A`** (코나미 커맨드)를 입력하면 멀티 모델 운용을 위한 **고급 AI 라우팅 패널**이 나타납니다.

## 🛡️ 주권과 개인정보 보호
- **로컬 주권**: AI나 TTS를 명시적으로 호출하지 않는 한 데이터가 당신의 공간을 떠나지 않습니다.
- **계정 불필요**: 아카이브는 브라우저의 `localStorage`에만 보관됩니다.

## 📚 추가 문의
상세한 구성 지침은 [큐레이터 가이드](docs/GUIDE.md)를 참조하세요.

## 📄 출처
[MIT License](LICENSE)
