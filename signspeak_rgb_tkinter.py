from tkinter import *
import cv2
from PIL import Image, ImageTk
import numpy as np
import threading
import mediapipe as mp
import pyttsx3
import time

# Initialize MediaPipe and text-to-speech
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils
engine = pyttsx3.init()

# Initialize GUI
app = Tk()
app.title("🧠 SignSpeak AI – RGB Tkinter Bomb")
app.geometry("1000x650")
app.config(bg="#0f0f0f")

# Animated header
header = Label(app, text="🎇 SignSpeak AI – RGB Bomb Edition 🎇", font=("Helvetica", 24, "bold"),
               fg="#39ff14", bg="#0f0f0f")
header.pack(pady=10)

# Webcam display
video_label = Label(app, bg="#0f0f0f")
video_label.pack()

# Sign display
sign_var = StringVar()
sign_var.set("🖐️ Detected Sign: Loading...")
sign_display = Label(app, textvariable=sign_var, font=("Helvetica", 18, "bold"), fg="#00ffff", bg="#0f0f0f")
sign_display.pack(pady=10)

# Function to predict sign
def get_sign(landmarks):
    y = [lm.y for lm in landmarks]
    folded = [y[8] > y[6], y[12] > y[10], y[16] > y[14], y[20] > y[18]]
    if all(folded): return "A"
    if not any(folded): return "B"
    if not folded[0] and folded[2] and folded[3]: return "C"
    if folded[1] and folded[2] and folded[3]: return "D"
    if folded == [True, True, True, True]: return "E"
    return "Unknown"

# Video capture thread
cap = cv2.VideoCapture(0)
last_spoken = ""
last_time = 0

def video_loop():
    global last_spoken, last_time
    while True:
        ret, frame = cap.read()
        if not ret:
            continue
        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                sign = get_sign(hand_landmarks.landmark)
                sign_var.set(f"🖐️ Detected Sign: {sign}")
                if sign != last_spoken and sign != "Unknown" and time.time() - last_time > 2:
                    last_spoken = sign
                    last_time = time.time()
                    engine.say(f"This is sign {sign}")
                    engine.runAndWait()

        # RGB overlay
        overlay = np.zeros_like(frame)
        h, w, _ = overlay.shape
        for i in range(0, w, 20):
            cv2.line(overlay, (i, 0), (i, h), (np.random.randint(255), np.random.randint(255), np.random.randint(255)), 1)

        frame = cv2.addWeighted(frame, 0.9, overlay, 0.1, 0)
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        imgtk = ImageTk.PhotoImage(image=img)
        video_label.imgtk = imgtk
        video_label.configure(image=imgtk)

# Run in separate thread
thread = threading.Thread(target=video_loop)
thread.daemon = True
thread.start()

app.mainloop()
