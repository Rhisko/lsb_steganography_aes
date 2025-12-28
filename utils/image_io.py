import cv2
import os

def load_image(path: str) -> cv2.Mat:
    img = cv2.imread(path, cv2.IMREAD_COLOR)
    if img is None:
        raise FileNotFoundError(f"Image not found: {path}")
    return img

def save_image(path: str, image) :
    cv2.imwrite(path, image)


def list_images(folder: str) -> list:
    return [f for f in os.listdir(folder) if f.lower().endswith((".png", ".jpg", ".jpeg"))]