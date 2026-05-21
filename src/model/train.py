import os
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau, ModelCheckpoint
from sklearn.utils.class_weight import compute_class_weight

from src.model.model_builder import build_model

# ===============================
# PATHS
# ===============================
BASE_DIR = "data/processed"
TRAIN_DIR = os.path.join(BASE_DIR, "train")
VAL_DIR = os.path.join(BASE_DIR, "val")

MODEL_DIR = "models"
os.makedirs(MODEL_DIR, exist_ok=True)

MODEL_PATH = os.path.join(MODEL_DIR, "efficientnetb3_best.h5")

# ===============================
# TRAINING PARAMETERS
# ===============================
IMG_SIZE = (300, 300)
BATCH_SIZE = 16
EPOCHS = 30
NUM_CLASSES = 10

# ===============================
# DATA GENERATORS
# ===============================
train_datagen = ImageDataGenerator(
    rescale=1.0 / 255,
    rotation_range=30,
    width_shift_range=0.1,
    height_shift_range=0.1,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode="nearest"
)

val_datagen = ImageDataGenerator(rescale=1.0 / 255)

train_generator = train_datagen.flow_from_directory(
    TRAIN_DIR,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode="categorical",
    shuffle=True
)

val_generator = val_datagen.flow_from_directory(
    VAL_DIR,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode="categorical",
    shuffle=False
)

# ===============================
# CLASS WEIGHTS (IMBALANCE HANDLING)
# ===============================
labels = train_generator.classes

class_weights = compute_class_weight(
    class_weight="balanced",
    classes=np.unique(labels),
    y=labels
)

class_weights = dict(enumerate(class_weights))
print("\nClass Weights:", class_weights)

# ===============================
# BUILD MODEL
# ===============================
model = build_model(num_classes=NUM_CLASSES)

# ===============================
# CALLBACKS
# ===============================
early_stop = EarlyStopping(
    monitor="val_loss",
    patience=5,
    restore_best_weights=True
)

reduce_lr = ReduceLROnPlateau(
    monitor="val_loss",
    factor=0.3,
    patience=3,
    min_lr=1e-6
)

checkpoint = ModelCheckpoint(
    MODEL_PATH,
    monitor="val_accuracy",
    save_best_only=True,
    verbose=1
)

# ===============================
# TRAIN MODEL
# ===============================
history = model.fit(
    train_generator,
    validation_data=val_generator,
    epochs=EPOCHS,
    class_weight=class_weights,
    callbacks=[early_stop, reduce_lr, checkpoint]
)

# ===============================
# FINAL ACCURACY OUTPUT
# ===============================
best_train_acc = max(history.history["accuracy"])
best_val_acc = max(history.history["val_accuracy"])

print("\n===============================")
print(f"✅ Best Training Accuracy: {best_train_acc * 100:.2f}%")
print(f"✅ Best Validation Accuracy: {best_val_acc * 100:.2f}%")
print(f"📦 Best Model Saved At: {MODEL_PATH}")
print("===============================\n")

# ===============================
# PLOT ACCURACY & LOSS
# ===============================
plt.figure(figsize=(12, 5))

# Accuracy
plt.subplot(1, 2, 1)
plt.plot(history.history["accuracy"], label="Training Accuracy")
plt.plot(history.history["val_accuracy"], label="Validation Accuracy")
plt.title("Accuracy Curve")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend()

# Loss
plt.subplot(1, 2, 2)
plt.plot(history.history["loss"], label="Training Loss")
plt.plot(history.history["val_loss"], label="Validation Loss")
plt.title("Loss Curve")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()

plt.tight_layout()
plt.show()