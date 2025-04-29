import cv2
import mediapipe as mp
import pyttsx3
import time

engine = pyttsx3.init()
engine.setProperty('rate', 150)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
last_spoken = ""
last_time = time.time()

def speak(text):
    global last_spoken, last_time
    if text != last_spoken or time.time() - last_time > 2:
        engine.say(f"This is sign {text}")
        engine.runAndWait()
        last_spoken = text
        last_time = time.time()

def get_finger_states(lm):
    tips = [8, 12, 16, 20]
    folded = []
    for tip in tips:
        folded.append(lm[tip].y > lm[tip - 2].y)
    return folded

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for hand in result.multi_hand_landmarks:
            lm = hand.landmark
            h, w, _ = frame.shape
            lm_px = [(int(p.x * w), int(p.y * h)) for p in lm]
            states = get_finger_states(lm)

            # Detect signs (simplified logic)
            sign = "Unknown"
            if all(states):         # All fingers folded → A
                sign = "A"
            elif not any(states):   # All fingers open → B
                sign = "B"
            elif states == [False, True, True, True]:  # Only index up → D
                sign = "D"
            elif states == [True, True, True, True]:   # Curved fingers → E
                sign = "E"
            elif states == [False, False, True, True]: # Shape like 'C'
                sign = "C"

            speak(sign)
            cv2.putText(frame, f"Sign: {sign}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX,
                        1.5, (0, 255, 0), 3)
            mp_draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("SignSpeak AI", frame)
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
