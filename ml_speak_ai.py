import cv2
import mediapipe as mp
import numpy as np
import pyttsx3
import pickle
import threading
import time

# === Load Pretrained Model ===
with open("signspeak_model.pkl", "rb") as f:
    model = pickle.load(f)

# === Setup TTS (non-blocking) ===
engine = pyttsx3.init()
engine.setProperty('rate', 150)
def speak_async(text):
    threading.Thread(target=lambda: [engine.say(text), engine.runAndWait()]).start()

# === MediaPipe Hands ===
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.75)
mp_draw = mp.solutions.drawing_utils

# === Webcam Setup ===
cap = cv2.VideoCapture(0)
prev_sign = ""
last_spoken = 0
cooldown = 1.5  # seconds

print("🟢 ML-Based SignSpeak AI Running... Show a sign!")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(frame_rgb)

    sign_pred = ""
    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)
            h, w, _ = frame.shape
            landmark_list = []

            for lm in handLms.landmark:
                landmark_list.extend([lm.x, lm.y])  # 42 features (21 x,y)

            if len(landmark_list) == 42:
                prediction = model.predict([landmark_list])[0]
                sign_pred = prediction

    # === Show Prediction ===
    if sign_pred:
        cv2.putText(frame, f"🖐 {sign_pred}", (30, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)
        if sign_pred != prev_sign or time.time() - last_spoken > cooldown:
            speak_async(sign_pred)
            prev_sign = sign_pred
            last_spoken = time.time()
    else:
        cv2.putText(frame, "No hand detected", (30, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # === Display Window ===
    cv2.imshow("SignSpeak AI - ML Powered", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
