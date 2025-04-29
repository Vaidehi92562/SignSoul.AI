# SignSoul.AI
# 🧠 SignSoul.ai — Real-Time Sign Language to Speech Converter

SignSoul.ai is an AI-powered sign language interpreter designed to help the deaf and mute community communicate more naturally. This system captures hand gestures via webcam, classifies them using a trained CNN model, and converts recognized signs into speech — all in real-time and directly from the browser.

![SignSoul Logo](logo.png) <!-- Replace with actual logo path -->

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

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/SignSoul.ai.git
cd SignSoul.ai
2. Install Python Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Run (Optional - Flask)
bash
Copy
Edit
python app.py
4. Run Frontend Only (Recommended)
Just open sign.html in your browser.
Ensure webcam permissions are enabled.

📊 Model Details
Input Size: 64×64 RGB images

Classes: A–Z + 10 frequent sign phrases

Accuracy: 91.8%

F1 Score: 91.4%

Training: 80/20 Train-Test Split

Frameworks: TensorFlow + Keras

📽️ Demo
👉 [Live Demo (if hosted)]
📹 Demo will be shown live during project presentation.

🔮 Future Enhancements
➕ Add dynamic gesture recognition (LSTM/Transformer)

🌍 Multilingual speech output (Hindi, Tamil, etc.)

📲 Mobile-ready deployment

😊 Facial expression detection

🧑‍🏫 Sign-learning dashboard for users

🗣️ Add reverse flow: Speech-to-sign translation

👩‍💻 Contributors
Ankita Mundra (RA2311003011145)

Rishika Dhanuka (RA2311003011165)

Vaidehi Mishra (RA2311003011168)

📜 License
This project is licensed under the MIT License.

⭐ Support Us
If you like this project, star ⭐ the repo and share your feedback!
Let’s build a more inclusive digital world together 💙


---

Let me know if you want me to generate:
- A `requirements.txt`
- A demo GIF or YouTube link preview code
- A deployment guide or badge for TensorFlow.js

All the best for your GitHub upload and the review! 💪
