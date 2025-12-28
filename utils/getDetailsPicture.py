import os
from PIL import Image
import pandas as pd
from config import INPUT_FOLDER, STEGO_FOLDER

image_info = []

def get_image_details(image_paths, status="input"):
    base_folder = STEGO_FOLDER if status == "stego" else INPUT_FOLDER
    
    for path in image_paths:
        image = f"{base_folder}/{path}"
        print(f"Analyzing image: {image}")
        try:
            with Image.open(image) as img:
                width, height = img.size
            file_size = os.path.getsize(image)
            image_info.append({
                "Filename": os.path.basename(path),
                "Resolution": f"{width}x{height}",
                "Width": width,
                "Height": height,
                "File Size (bytes)": file_size
            })
        except Exception as e:
            print(f"Error reading {path}: {e}")

    df = pd.DataFrame(image_info)
    print("\n📊 Informasi Gambar:")
    print(df)

    output_csv = f"outputs/image_analysis_result_{status}.csv"
    df.to_csv(output_csv, index=False)
    print(f"\n✅ Hasil disimpan ke: {output_csv}")
    return image_info
