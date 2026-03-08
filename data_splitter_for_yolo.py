import os
import random
import shutil

source = "drone_dataset_yolo/dataset_txt"

train_img = "final_dataset/images/train"
val_img = "final_dataset/images/val"
train_lbl = "final_dataset/labels/train"
val_lbl = "final_dataset/labels/val"

os.makedirs(train_img, exist_ok=True)
os.makedirs(val_img, exist_ok=True)
os.makedirs(train_lbl, exist_ok=True)
os.makedirs(val_lbl, exist_ok=True)

images = [img for img in os.listdir(source) if img.endswith(".jpg")]

random.shuffle(images)

split = int(len(images) * 0.8)

train = images[:split]
val = images[split:]

for img in train:
    lbl = img.replace(".jpg", ".txt")
    shutil.move(f"{source}/{img}", f"{train_img}/{img}")
    shutil.move(f"{source}/{lbl}", f"{train_lbl}/{lbl}")

for img in val:
    lbl = img.replace(".jpg", ".txt")
    shutil.move(f"{source}/{img}", f"{val_img}/{img}")
    shutil.move(f"{source}/{lbl}", f"{val_lbl}/{lbl}")
    
print('All done')