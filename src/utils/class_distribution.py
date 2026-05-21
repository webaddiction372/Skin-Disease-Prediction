import os

BASE_DIR = "data/raw/images"

for cls in os.listdir(BASE_DIR):
    class_dir = os.path.join(BASE_DIR, cls)
    if os.path.isdir(class_dir):
        count = len(os.listdir(class_dir))
        print(f"{cls}: {count}")