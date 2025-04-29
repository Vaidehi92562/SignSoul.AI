# SignSoul.AI
# 🧠 SignSoul.ai — Real-Time Sign Language to Speech Converter

SignSoul.ai is an AI-powered sign language interpreter designed to help the deaf and mute community communicate more naturally. This system captures hand gestures via webcam, classifies them using a trained CNN model, and converts recognized signs into speech — all in real-time and directly from the browser.

---

## 🔍 Project Overview

- 🖐️ **Input:** Live hand gestures (A–Z + 10 common signs)
- 🎯 **Goal:** Translate sign language into **spoken audio**
- 🖥️ **Tech:** MediaPipe + TensorFlow/Keras + HTML/CSS/JS
- 🌐 **Deployment:** Browser-based (TensorFlow.js in progress)
- 📣 **Output:** Audio response using Web Speech API or pyttsx3

---

## 💡 Features

- ✅ Real-time gesture recognition using webcam
- 🎨 Clean, interactive front-end UI (`sign.html`)
- 🧠 Custom-trained CNN model (.h5)
- 🔊 Instant text-to-speech conversion
- 💻 Offline functionality (no Flask required)
- 🔄 Future support for multilingual output & dynamic gestures

---

## 🧰 Tech Stack

| Component           | Tool/Library         |
|--------------------|----------------------|
| Programming        | Python, JavaScript   |
| CV & Tracking      | MediaPipe Hands      |
| Model Training     | TensorFlow, Keras    |
| Speech Output      | Web Speech API / pyttsx3 |
| Frontend           | HTML, CSS, JavaScript|
| Model Deployment   | (In progress) TensorFlow.js |

---

## 📁 Folder Structure

├── sign.html # Main frontend ├── static/ # CSS and assets ├── model/ # Trained CNN model (.h5) ├── scripts/ # JS for webcam & prediction ├── app.py # (Optional) Flask backend (deprecated) ├── requirements.txt # Python dependencies └── README.md # Project documentation

yaml
Copy
Edit

---


### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/SignSoul.ai.git
cd SignSoul.ai

