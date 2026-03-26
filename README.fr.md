[English](README.en.md) | [简体中文](README.md) | [繁體中文](README.zh-Hant.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Español](README.es.md) | Français | [Italiano](README.it.md)

# 🧊 Smoothie Reader (Reader3)

> "Lorsque la technologie est démocratisée par l'IA, l'esthétique et le design centré sur l'humain deviennent les ultimes différenciateurs."

Inspiré par le [prototype de lecteur minimaliste](https://x.com/karpathy/status/1990577951671509438) d'Andrej Karpathy, Smoothie Reader est un environnement commissarié et augmenté par l'IA, conçu pour une lecture profonde. En tant que commissaire d'exposition d'art contemporain basé à Shanghai, j'ai fait évoluer le flux de travail original « copier-coller vers le LLM » en un dialogue fluide et transparent entre le lecteur, le texte et la machine.

🏛️ **L'Exposition Inaugurale : Méditations**. Pour honorer l'esprit de contemplation focalisée, ce dépôt est pré-chargé avec les « Méditations » de Marc Aurèle (via Project Gutenberg).

<div align="center">
  <img src="assets/library.jpg" width="800" alt="Library"><br>
  <sub>Votre bibliothèque personnelle en un coup d'œil</sub>
</div>

## ✨ La Vision du Commissaire

Alors que la plupart des lecteurs n'affichent que du texte, Smoothie Reader traite chaque page comme une pièce d'exposition, transformant la lecture en une expérience intellectuelle holistique :

- 🔍 **Découverte Intuitive** : Surlignez n'importe quel texte pour révéler la barre d'action. Prise en charge intégrée d'**ECDICT** (Anglais) et de dictionnaires chinois hors ligne.
- 🤖 **Le Dialogue Augmenté** :
  - **Traduction Narrative** : Traductions contextuelles de haute qualité élégamment intégrées au texte.
  - **Le Compagnon Numérique** : Un assistant IA en barre latérale prenant en charge le dialogue en streaming et la mémoire multi-tours pour un engagement intellectuel profond.
  - **Connectivité Mondiale** : Intégration transparente avec plus de 20 fournisseurs, dont Gemini, OpenAI, Claude et DeepSeek.

<div align="center">
  <img src="assets/reader_AItools.jpg" width="800" alt="AI Tools"><br>
  <sub>Barre de sélection · Traduction en ligne · Panneau latéral du compagnon IA</sub>
</div>

- 🔊 **Contemplation Sonore (TTS)** : Propulsé par Edge-TTS, offrant plus de 90 voix pour insuffler la vie au mot écrit.
- ✏️ **L'Archive** : Surlignage esthétique en 5 couleurs, annotations en ligne et signets persistants—le tout préservé dans votre **coffre-fort local**.

<div align="center">
  <img src="assets/reader_catelog.jpg" width="800" alt="Reading Layout"><br>
  <sub>Lecture en 3 colonnes : navigation ToC · Texte immersif · Surlignages multicolores</sub>
</div>

- 🎨 **Esthétique Minimaliste** : 6 thèmes sélectionnés et une mise en page flexible à 3 colonnes, conçue pour la concentration et la clarté sur tous les appareils.

<div align="center">
  <img src="assets/reader_setting.jpg" width="800" alt="Settings"><br>
  <sub>Thèmes, typographie, dictionnaires, modèles IA — configuration tout-en-un</sub>
</div>

## 🚀 L'Installation

Ce projet utilise strictement [uv](https://docs.astral.sh/uv/) pour l'orchestration de l'environnement, garantissant une performance fluide et isolée.

### 1. Préparation
Assurez-vous que Python 3.9+ est disponible. Installez l'orchestrateur `uv` :
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Ouverture de l'Exposition
```bash
# Importez votre première pièce (ex. Dracula)
uv run reader3.py dracula.epub

# Lancez l'environnement
uv run server.py
```
Accédez au lecteur sur : 👉 **http://localhost:8123**

### 3. Activation de l'IA
Entrez dans l'interface de lecture, naviguez vers **Paramètres (Settings)** et configurez vos **Fournisseurs d'IA**. Connectez votre essence à la machine (ex. [obtenez une clé Gemini gratuite](https://aistudio.google.com/apikey)).

> [!TIP]
> **🚀 Le Passage Secret** : N'importe où sur la page, effectuez le rituel : **`↑ ↑ ↓ ↓ ← → ← → B A`** (Code Konami) pour dévoiler le **Panneau de Routage IA Avancé** pour l'orchestration multi-modèles.

## 🛡️ Souveraineté et Confidentialité
- **Souveraineté Locale** : Aucune donnée ne quitte votre sanctuaire, sauf si vous invoquez explicitement l'IA ou le TTS.
- **Sans Compte** : Vos archives restent exclusivement dans le `localStorage` de votre navigateur.

## 📚 Enquête Complémentaire
Pour des instructions d'orchestration détaillées, consultez le [Guide du Commissaire](docs/GUIDE.md).

## 📄 Provenance
[MIT License](LICENSE)
