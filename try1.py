import cv2
import mediapipe as mp
import pyttsx3
import time
import tkinter as tk
from PIL import Image, ImageTk

# Initialize TTS
engine = pyttsx3.init()
engine.setProperty('rate', 150)

# MediaPipe Setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

# Webcam
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Globals
last_spoken = ""
last_time = time.time()
sign_display = "🤖"

def speak(text):
    global last_spoken, last_time
    if text != last_spoken or time.time() - last_time > 2:
        engine.say(f"This is sign {text}")
        engine.runAndWait()
        last_spoken = text
        last_time = time.time()

def get_finger_states(lm):
    tips = [8, 12, 16, 20]
    return [lm[tip].y > lm[tip - 2].y for tip in tips]

def detect_sign(frame):
    global sign_display
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)
    sign = "🤖"

    if result.multi_hand_landmarks:
        for hand in result.multi_hand_landmarks:
            lm = hand.landmark
            states = get_finger_states(lm)

            if all(states): sign = "A"
            elif not any(states): sign = "B"
            elif states == [False, False, True, True]: sign = "C"
            elif states == [False, True, True, True]: sign = "D"
            elif states == [True, True, True, True]: sign = "E"

            speak(sign)
            mp_draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)
            sign_display = sign

    return frame

def update_gui():
    ret, frame = cap.read()
    if not ret:
        return

    frame = cv2.flip(frame, 1)
    frame = detect_sign(frame)
    img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    imgtk = ImageTk.PhotoImage(image=img)
    video_label.imgtk = imgtk
    video_label.configure(image=imgtk)
    sign_label.config(text=f"👉 Detected Sign: {sign_display} 👈")
    root.after(10, update_gui)

# =================== GUI =====================

root = tk.Tk()
root.title("🤖 SignSpeak AI – Gesture to Voice")
root.geometry("1100x850")
root.config(bg="#0b0f1a")

# 🔹 Stylish Title
lbl_title = tk.Label(root, text="SignSpeak AI – Gesture to Voice",
                     font=("Segoe UI Semibold", 32, "bold"),
                     bg="#0b0f1a", fg="#00f0ff")
lbl_title.pack(pady=30)

# 🟡 Detected Sign Display
sign_label = tk.Label(root, text="👉 Detected Sign: 🤖 👈",
                      font=("Segoe UI", 24, "bold"),
                      bg="#0b0f1a", fg="#fcd900")
sign_label.pack(pady=20)

# 🖼️ Webcam Display with Glowing Frame
frame_wrap = tk.Frame(root, bg="#00f0ff", bd=8, relief="groove", highlightbackground="#00f0ff", highlightthickness=2)
frame_wrap.pack(pady=10)

video_label = tk.Label(frame_wrap, bg="#0d111c")
video_label.pack()

# ✨ Footer
footer = tk.Label(root, text="✨ Made with ❤️ by SignSpeak AI for Accessibility ✨",
                  font=("Segoe UI", 12), bg="#0b0f1a", fg="#808080")
footer.pack(pady=30)

# Start GUI Loop
update_gui()
root.mainloop()

# Cleanup
cap.release()
cv2.destroyAllWindows()
