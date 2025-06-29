import os
import shutil

VAL_DIR = "../../datasets/tiny-imagenet-200/val"
ANNOTATIONS_FILE = "../../datasets/tiny-imagenet-200/val/val_annotations.txt"
IMAGES_DIR = "images"
IMAGES_DIR = os.path.join(VAL_DIR,IMAGES_DIR)

#Read annotations file and store filenames with corresponding class label
annotations = {}

with open(ANNOTATIONS_FILE, "r") as f:
    for line in f.readlines():
        parts = line.strip().split("\t")
        filename = parts[0]
        class_label = parts[1]
        annotations[filename] = class_label

#Create subfolders and move images

for filename, class_label in annotations.items():
    class_dir = os.path.join(VAL_DIR, class_label)

    if not os.path.exists(class_dir):
        os.makedirs(class_dir)

    src_path = os.path.join(IMAGES_DIR, filename)
    dst_path = os.path.join(class_dir, filename)

    if os.path.exists(src_path):
        shutil.move(src_path, dst_path)

#Delete the now-empty images folder
if os.path.exists(IMAGES_DIR) and len(os.listdir(IMAGES_DIR)) == 0:
    os.rmdir(IMAGES_DIR)

print("✅ Validation set reorganized into class-based folders.")
