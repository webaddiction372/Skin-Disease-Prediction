import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image

# =========================
# CLASS NAMES
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
    "Seborrheic_Keratoses",
    "Viral_Infection"
]

# =========================
# PATH
# =========================
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")) 
MODEL_PATH = os.path.join(PROJECT_ROOT, "models", "final_model.h5")

IMG_SIZE = (224, 224)

# =========================
# BUILD MODEL
# =========================
def build_model(): 
    base_model = tf.keras.applications.EfficientNetB0(
        input_shape=(224, 224, 3),
        include_top=False,
        weights=None
    )

    x = base_model.output
    x = tf.keras.layers.GlobalAveragePooling2D()(x)
    x = tf.keras.layers.Dense(128, activation='relu')(x)
    output = tf.keras.layers.Dense(len(CLASS_NAMES), activation='softmax')(x)

    return tf.keras.Model(inputs=base_model.input, outputs=output) # return model architecture

model = build_model()

try:
    model.load_weights(MODEL_PATH, by_name=True, skip_mismatch=True)
    print("✅ Model Loaded")
except Exception as e:
    print("❌ Model load error:", e)

# =========================
# PREDICTION FUNCTION  
# =========================

def predict_image(img_path): # ML predict image and return result
    img = image.load_img(img_path, target_size=IMG_SIZE) # Load and preprocess image
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0) # Add batch dimension for model input

    preds = model.predict(img_array)
    idx = int(np.argmax(preds[0]))
    confidence = float(preds[0][idx])

    return {
        "predicted_disease": CLASS_NAMES[idx],
        "confidence": round(confidence * 100, 2),
        "assistance": {
            "description": "AI-based prediction result",
            "care_tips": [
                "Consult a dermatologist",
                "Avoid self-medication",
                "Maintain hygiene"
            ]
        }
    }