import cv2
import mediapipe as mp
import pyttsx3
import time
import tkinter as tk
from PIL import Image, ImageTk

# Initialize voice engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)

# MediaPipe hand setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

# Webcam
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Global state
last_spoken = ""
last_time = time.time()
sign_display = ""

# Speak function
def speak(text):
    global last_spoken, last_time
    if text != last_spoken or time.time() - last_time > 2:
        engine.say(f"This is sign {text}")
        engine.runAndWait()
        last_spoken = text
        last_time = time.time()

# Finger detection
def get_finger_states(lm):
    tips = [8, 12, 16, 20]
    folded = []
    for tip in tips:
        folded.append(lm[tip].y > lm[tip - 2].y)
    return folded

# Sign detection
def detect_sign(frame):
    global sign_display
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)
    sign = "Unknown"

    if result.multi_hand_landmarks:
        for hand in result.multi_hand_landmarks:
            lm = hand.landmark
            states = get_finger_states(lm)

            if all(states):
                sign = "A"
            elif not any(states):
                sign = "B"
            elif states == [False, False, True, True]:
                sign = "C"
            elif states == [False, True, True, True]:
                sign = "D"
            elif states == [True, True, True, True]:
                sign = "E"
            else:
                sign = "Unknown"

            speak(sign)
            mp_draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)
            sign_display = sign

    return frame

# GUI update loop
def update_gui():
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        return

    frame = cv2.flip(frame, 1)
    frame = detect_sign(frame)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(frame_rgb)
    imgtk = ImageTk.PhotoImage(image=img)
    lbl_video.imgtk = imgtk
    lbl_video.configure(image=imgtk)
    lbl_sign.config(text=f"👉 Detected Sign: {sign_display} 👈")
    window.after(10, update_gui)

# GUI setup
window = tk.Tk()
window.title("✨ SignSpeak AI ✨")
window.geometry("1000x800")
window.config(bg="#0d0d1a")

lbl_title = tk.Label(window, text="💬 SignSpeak AI – Gesture to Voice 🎤",
                     font=("Comic Sans MS", 28, "bold"), bg="#0d0d1a", fg="#00fff7")
lbl_title.pack(pady=20)

lbl_sign = tk.Label(window, text="👉 Detected Sign: 👈",
                    font=("Helvetica", 22, "bold"), bg="#0d0d1a", fg="#ffff00")
lbl_sign.pack(pady=10)

frame_border = tk.Frame(window, bg="#00fff7", bd=10, relief="ridge")
frame_border.pack(pady=10)

lbl_video = tk.Label(frame_border, bg="#000")
lbl_video.pack()

lbl_footer = tk.Label(window, text="❤ Made with Love | SignSpeak AI for Accessibility ✨",
                      font=("Courier New", 12), bg="#0d0d1a", fg="#999999")
lbl_footer.pack(pady=20)

# Start loop
update_gui()
window.mainloop()

# Cleanup
cap.release()
cv2.destroyAllWindows()
