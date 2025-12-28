from utils.steganography import embed_data, extract_data
from utils.image_io import load_image, save_image, list_images
from utils.encryption import encrypt_data, decrypt_data
from utils.metrics import calculate_psnr, calculate_mse
from config import SECRET_PATH, INPUT_FOLDER, STEGO_FOLDER, OUTPUT_FOLDER , PASSWORD
import os

def run():

    with open(SECRET_PATH, "rb") as f:
        raw_data = f.read()
    encrypted = encrypt_data(raw_data, PASSWORD)

    images = list_images(INPUT_FOLDER)
    for img_file in images:
        print(f"[*] Processing {img_file}... | Size: {os.path.getsize(os.path.join(INPUT_FOLDER, img_file))} bytes")
        input_path = os.path.join(INPUT_FOLDER, img_file)
        img = load_image(input_path)

        try:
            stego_img = embed_data(img, encrypted)
        except ValueError as ve:
            print(f"[!] Skipping {img_file}: {ve}")
            continue

        stego_path = os.path.join(STEGO_FOLDER, f"stego_{img_file}")
        save_image(stego_path, stego_img)
        print(f"    → Stego image saved: {stego_path} | Size: {os.path.getsize(stego_path)} bytes")

        # Ekstraksi dan dekripsi
        stego_loaded = load_image(stego_path)
        try:
            extracted = extract_data(stego_loaded)
            decrypted = decrypt_data(extracted, PASSWORD)
        except Exception as e:
            print(f"[!] Error during extraction/decryption: {e}")
            continue

        # Simpan hasil
        output_path = os.path.join(OUTPUT_FOLDER, f"recovered_{os.path.splitext(img_file)[0]}.txt")
        with open(output_path, "wb") as f:
            f.write(decrypted)

        # # Evaluasi
        # psnr = calculate_psnr(img, stego_img)
        # mse = calculate_mse(img, stego_img)
        # print(f"    → PSNR: {psnr:.2f} dB | MSE: {mse:.4f} | Saved: {output_path}")

if __name__ == "__main__":
    run()
