import os
import shutil
import random

# Paths
SOURCE_DIR = "data/raw/images"
TARGET_DIR = "data/processed"

# Train / Validation / Test split ratio
SPLIT_RATIO = {
    "train": 0.7,
    "val": 0.15,
    "test": 0.15
}

def split_dataset():
    random.seed(42)

    for class_name in os.listdir(SOURCE_DIR):
        class_path = os.path.join(SOURCE_DIR, class_name)

        if not os.path.isdir(class_path):
            continue

        images = [
            img for img in os.listdir(class_path)
            if img.lower().endswith((".jpg", ".jpeg", ".png"))
        ]

        random.shuffle(images)
        total_images = len(images)

        train_end = int(SPLIT_RATIO["train"] * total_images)
        val_end = train_end + int(SPLIT_RATIO["val"] * total_images)

        splits = {
            "train": images[:train_end],
            "val": images[train_end:val_end],
            "test": images[val_end:]
        }

        for split, split_images in splits.items():
            split_dir = os.path.join(TARGET_DIR, split, class_name)
            os.makedirs(split_dir, exist_ok=True)

            for img in split_images:
                src = os.path.join(class_path, img)
                dst = os.path.join(split_dir, img)
                shutil.copy2(src, dst)

        print(f"✔ {class_name}: {total_images} images split")

    print("\n✅ Dataset successfully split into train / val / test")

if __name__ == "__main__":
    split_dataset()