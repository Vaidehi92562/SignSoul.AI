import os
import cv2
import numpy as np

labels = ['A', 'B', 'C', 'D', 'E']
IMG_SIZE = 64
DATA_DIR = "sign_data"

os.makedirs(DATA_DIR, exist_ok=True)

# Create 100 dummy images per class
for label in labels:
    class_dir = os.path.join(DATA_DIR, label)
    os.makedirs(class_dir, exist_ok=True)
    
    for i in range(100):
        img = np.zeros((IMG_SIZE, IMG_SIZE, 3), dtype=np.uint8)
        
        if label == 'A':
            img[:, :] = [255, 0, 0]      # Red
        elif label == 'B':
            img[:, :] = [0, 255, 0]      # Green
        elif label == 'C':
            img[:, :] = [0, 0, 255]      # Blue
        elif label == 'D':
            img[:, :] = [255, 255, 0]    # Yellow
        elif label == 'E':
            img[:, :] = [255, 0, 255]    # Magenta
        
        cv2.imwrite(f"{class_dir}/{label}_{i}.png", img)

print("✅ Dummy sign data generated successfully.")
