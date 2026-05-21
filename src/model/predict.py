import os
import sys
import random
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image

# =========================
# PATHS
# =========================
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

MODEL_PATH = os.path.join(PROJECT_ROOT, "models", "skin_model_best.h5")
DATASET_PATH = os.path.join(PROJECT_ROOT, "data", "processed", "test")

# 🔥 MUST MATCH TRAINING
IMG_SIZE = (300, 300)

# =========================
# LOAD MODEL
# =========================
if not os.path.exists(MODEL_PATH):
    print("Model file not found:", MODEL_PATH)
    sys.exit(1)

model = tf.keras.models.load_model(MODEL_PATH)
print("Model loaded successfully")

# =========================
# RANDOM IMAGE SELECTION
# =========================
class_folders = [
    d for d in os.listdir(DATASET_PATH)
    if os.path.isdir(os.path.join(DATASET_PATH, d))
]

random_class = random.choice(class_folders)
class_path = os.path.join(DATASET_PATH, random_class)

images = [
    f for f in os.listdir(class_path)
    if f.lower().endswith((".jpg", ".png", ".jpeg"))
]

random_image = random.choice(images)
IMAGE_PATH = os.path.join(class_path, random_image)

print("Random Image Selected:", IMAGE_PATH)

# =========================
# LOAD & PREPROCESS IMAGE
# =========================
img = image.load_img(IMAGE_PATH, target_size=IMG_SIZE)
img_array = image.img_to_array(img)
img_array = img_array / 255.0
img_array = np.expand_dims(img_array, axis=0)

# =========================
# PREDICTION
# =========================
predictions = model.predict(img_array)
predicted_index = np.argmax(predictions[0])
confidence = predictions[0][predicted_index]

# =========================
# CLASS NAMES (MUST MATCH TRAINING ORDER)
# =========================
CLASS_NAMES = [
    "Atopic_Dermatitis",
    "Basal_Cell_Carcinoma",
    "Benign_Keratosis",
    "Eczema",
    "Fungal_Infection",
    "Melanocytic_Nevi",
    "Melanoma",
    "Psoriasis",
    "Seborrheic_Keratosis",
    "Viral_Infection"
]

# =========================
# OUTPUT
# =========================
print("\nPrediction Result")
print("-----------------")
print("Actual Class Folder :", random_class)
print("Predicted Disease   :", CLASS_NAMES[predicted_index])
print("Confidence          :", round(confidence * 100, 2), "%")