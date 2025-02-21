# 🚀 AI Voice Assistant

## 🔥 Overview
AI Voice Assistant is a personal project designed to bring seamless voice interaction to your Linux environment. With speech recognition, AI-driven responses, and command execution capabilities, this assistant enhances your workflow while keeping things natural and intuitive. It was **developed and tested exclusively on Arch Linux**.

## 🛠 Features
- 🎙 **Speech Recognition** – Converts spoken words into text using `speech_recognition`.
- 🤖 **AI-Powered Responses** – Uses **Google AI Studio** (Gemini API) for intelligent conversations.
- ⚙ **System Commands** – Executes system commands when triggered.
- 🔊 **Text-to-Speech** – Replies with a natural-sounding voice using `edge_tts`.
- 🎭 **Custom Processing** – Removes unnecessary characters like emojis and asterisks from responses.

## 💡 Why Use This?
- **Free & Open-Source** – Completely free to use, modify, and enhance.
- **Personal Development** – Created as a personal assistant, optimized for Arch Linux.
- **AI-Powered** – Leverages cutting-edge AI for better interactions.
- **Voice-Controlled** – Hands-free control for better efficiency.

## 🚀 Installation & Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/Bebrowskiy/CyberEcho.git
   cd CyberEcho
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Set up your API key in `config.py`:
   ```python
   API_KEY = "your_google_ai_studio_api_key"
   ```
4. Run the assistant:
   ```sh
   python main.py
   ```

## 🏆 Acknowledgments
This project utilizes:
- [Google AI Studio (Gemini)](https://ai.google.dev/)
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [Edge TTS](https://github.com/rany2/edge-tts)
- [Arch Linux](https://archlinux.org/)

## 📜 License
This project is **100% free** and open-source. Use it however you like!

---
⚡ *Developed & tested exclusively on Arch Linux* ⚡

