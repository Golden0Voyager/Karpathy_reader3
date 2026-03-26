[English](README.en.md) | [简体中文](README.md) | [繁體中文](README.zh-Hant.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Español](README.es.md) | [Français](README.fr.md) | Italiano

# 🧊 Smoothie Reader (Reader3)

> "Quando la tecnologia viene democratizzata dall'IA, l'estetica e il design incentrato sull'uomo diventano i differenziatori finali."

Ispirato al [prototipo di lettore minimalista](https://x.com/karpathy/status/1990577951671509438) di Andrej Karpathy, Smoothie Reader è un ambiente curato e aumentato dall'IA progettato per la lettura profonda. Come curatore d'arte contemporanea con base a Shanghai, ho evoluto il flusso di lavoro originale "copia-incolla verso l'LLM" in un dialogo fluido e senza soluzione di continuità tra il lettore, il testo e la macchina.

🏛️ **La Mostra Inaugurale: Meditazioni**. Per onorare lo spirito di contemplazione focalizzata, questo repository include pre-caricato "Meditazioni" di Marco Aurelio (via Project Gutenberg).

<div align="center">
  <img src="assets/library.jpg" width="800" alt="Library"><br>
  <sub>La tua biblioteca personale a colpo d'occhio</sub>
</div>

## ✨ La Visione del Curatore

Mentre la maggior parte dei lettori visualizza solo il testo, Smoothie Reader tratta ogni pagina come un'esposizione, trasformando la lettura in un'esperienza intellettuale olistica:

- 🔍 **Scoperta Intuitiva**: Evidenzia qualsiasi testo per rivelare la barra delle azioni. Supporto integrato per **ECDICT** (Inglese) e dizionari cinesi offline.
- 🤖 **Il Dialogo Aumentato**:
  - **Traduzione Narrativa**: Traduzioni contestuali di alta qualità elegantemente incorporate nel testo.
  - **Il Compagno Digitale**: Un assistente IA nella barra laterale che supporta il dialogo in streaming e la memoria multi-turno per un profondo coinvolgimento intellettuale.
  - **Connettività Globale**: Perfettamente integrato con oltre 20 provider tra cui Gemini, OpenAI, Claude e DeepSeek.

<div align="center">
  <img src="assets/reader_AItools.jpg" width="800" alt="AI Tools"><br>
  <sub>Barra di selezione · Traduzione in linea · Pannello laterale del compagno IA</sub>
</div>

- 🔊 **Contemplazione Sonora (TTS)**: Alimentato da Edge-TTS, offre oltre 90 voci per dare vita alla parola scritta.
- ✏️ **L'Archivio**: Evidenziazione estetica in 5 colori, annotazioni in linea e segnalibri persistenti—tutto conservato nel tuo **caveau locale**.

<div align="center">
  <img src="assets/reader_catelog.jpg" width="800" alt="Reading Layout"><br>
  <sub>Lettura a 3 colonne: navigazione ToC · Testo immersivo · Evidenziazioni multicolore</sub>
</div>

- 🎨 **Estetica Minimalista**: 6 temi curati e un layout flessibile a 3 colonne, progettato per la concentrazione e la chiarezza su tutti i dispositivi.

<div align="center">
  <img src="assets/reader_setting.jpg" width="800" alt="Settings"><br>
  <sub>Temi, tipografia, dizionari, modelli IA — configurazione tutto in uno</sub>
</div>

## 🚀 L'Installazione

Questo progetto utilizza rigorosamente [uv](https://docs.astral.sh/uv/) per l'orchestrazione dell'ambiente, garantendo prestazioni fluide e isolate.

### 1. Preparazione
Assicurati che Python 3.9+ sia disponibile. Installa l'orchestratore `uv`:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Apertura della Mostra
```bash
# Importa il tuo primo pezzo (es. Dracula)
uv run reader3.py dracula.epub

# Avvia l'ambiente
uv run server.py
```
Accedi al lettore su: 👉 **http://localhost:8123**

### 3. Attivazione dell'IA
Entra nell'interfaccia di lettura, vai su **Impostazioni (Settings)** e configura i tuoi **AI Provider**. Connetti la tua essenza alla macchina (es. [ottieni una Gemini Key gratuita](https://aistudio.google.com/apikey)).

> [!TIP]
> **🚀 Il Passaggio Segreto**: In qualsiasi punto della pagina, esegui il rito: **`↑ ↑ ↓ ↓ ← → ← → B A`** (Codice Konami) per svelare il **Pannello Avanzato di Routing IA** per l'orchestrazione multi-modello.

## 🛡️ Sovranità e Privacy
- **Sovranità Locale**: Nessun dato lascia il tuo santuario a meno che tu non invochi esplicitamente l'IA o il TTS.
- **Senza Account**: I tuoi archivi rimangono esclusivamente nel `localStorage` del tuo browser.

## 📚 Ulteriori Informazioni
Per istruzioni dettagliate sull'orchestrazione, consulta la [Guida del Curatore](docs/GUIDE.md).

## 📄 Provenienza
[MIT License](LICENSE)
