[English](README.en.md) | [简体中文](README.md) | [繁體中文](README.zh-Hant.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | Español | [Français](README.fr.md) | [Italiano](README.it.md)

# 🧊 Smoothie Reader (Reader3)

> "Cuando la tecnología es democratizada por la IA, la estética y el diseño centrado en el ser humano se convierten en los diferenciadores definitivos."

Inspirado por el [prototipo de lector minimalista](https://x.com/karpathy/status/1990577951671509438) de Andrej Karpathy, Smoothie Reader es un entorno curado y aumentado por IA diseñado para una lectura profunda. Como curador de arte contemporáneo establecido en Shanghái, he evolucionado el flujo de trabajo original de "copiar y pegar al LLM" hacia un diálogo fluido y sin interrupciones entre el lector, el texto y la máquina.

🏛️ **La Exhibición Inaugural: Meditaciones**. Para honrar el espíritu de contemplación enfocada, este repositorio viene precargado con "Meditaciones" de Marco Aurelio (vía Project Gutenberg).

<div align="center">
  <img src="assets/library.jpg" width="800" alt="Library"><br>
  <sub>Tu biblioteca personal de un vistazo</sub>
</div>

## ✨ La Visión Curatorial

Mientras que la mayoría de los lectores solo muestran texto, Smoothie Reader trata cada página como una exhibición, transformando la lectura en una experiencia intelectual holística:

- 🔍 **Descubrimiento Intuitivo**: Resalte cualquier texto para revelar la barra de acciones. Soporte integrado para **ECDICT** (Inglés) y diccionarios chinos offline.
- 🤖 **El Diálogo Aumentado**:
  - **Traducción Narrativa**: Traducciones contextuales de alta calidad elegantemente incrustadas dentro del texto.
  - **El Compañero Digital**: Un asistente de IA en la barra lateral que admite diálogos en streaming y memoria de múltiples turnos para un compromiso intelectual profundo.
  - **Conectividad Global**: Integrado perfectamente con más de 20 proveedores, incluidos Gemini, OpenAI, Claude y DeepSeek.

<div align="center">
  <img src="assets/reader_AItools.jpg" width="800" alt="AI Tools"><br>
  <sub>Barra de selección · Traducción en línea · Panel lateral del compañero IA</sub>
</div>

- 🔊 **Contemplación Sonora (TTS)**: Potenciado por Edge-TTS, ofreciendo más de 90 voces para dar vida a la palabra escrita.
- ✏️ **El Archivo**: Resaltado estético de 5 colores, anotaciones en línea y marcadores persistentes—todo preservado en su **bóveda local**.

<div align="center">
  <img src="assets/reader_catelog.jpg" width="800" alt="Reading Layout"><br>
  <sub>Lectura en 3 columnas: navegación ToC · Texto inmersivo · Resaltados multicolor</sub>
</div>

- 🎨 **Estética Minimalista**: 6 temas curados y un diseño flexible de 3 columnas, diseñado para el enfoque y la claridad en todos los dispositivos.

<div align="center">
  <img src="assets/reader_setting.jpg" width="800" alt="Settings"><br>
  <sub>Temas, tipografía, diccionarios, modelos IA — configuración todo en uno</sub>
</div>

## 🚀 La Instalación

Este proyecto utiliza estrictamente [uv](https://docs.astral.sh/uv/) para la orquestación del entorno, asegurando un rendimiento fluido y aislado.

### 1. Preparación
Asegúrese de tener Python 3.9+ disponible. Instale el orquestador `uv`:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Apertura de la Exhibición
```bash
# Importe su primera pieza (ej., Dracula)
uv run reader3.py dracula.epub

# Inicie el entorno
uv run server.py
```
Acceda al lector en: 👉 **http://localhost:8123**

### 3. Activación de la IA
Ingrese a la interfaz de lectura, navegue a **Configuración (Settings)** y configure sus **Proveedores de IA**. Conecte su esencia a la máquina (ej., [obtenga una Gemini Key gratis](https://aistudio.google.com/apikey)).

> [!TIP]
> **🚀 El Pasaje Secreto**: En cualquier lugar de la página, realice el ritual: **`↑ ↑ ↓ ↓ ← → ← → B A`** (Código Konami) para desvelar el **Panel Avanzado de Enrutamiento de IA** para la orquestación multimodelo.

## 🛡️ Soberanía y Privacidad
- **Soberanía Local**: Ningún dato sale de su santuario a menos que invoque explícitamente la IA o el TTS.
- **Sin Cuenta**: Sus archivos permanecen exclusivamente en el `localStorage` de su navegador.

## 📚 Consulta Adicional
Para instrucciones detalladas de orquestación, consulte la [Guía del Curador](docs/GUIDE.md).

## 📄 Procedencia
[MIT License](LICENSE)
