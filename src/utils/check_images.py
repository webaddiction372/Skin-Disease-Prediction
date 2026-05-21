import os
from PIL import Image

BASE_DIR = "data/raw/images"

bad_images = []

for cls in os.listdir(BASE_DIR):
    class_dir = os.path.join(BASE_DIR, cls)
    if not os.path.isdir(class_dir):
        continue

    for img in os.listdir(class_dir):
        img_path = os.path.join(class_dir, img)
        try:
            with Image.open(img_path) as im:
                im.verify()
        except:
            bad_images.append(img_path)

print(f"Corrupted images found: {len(bad_images)}")

for img in bad_images:
    print(img)