from utils.steganography import embed_data, extract_data
from utils.image_io import load_image, save_image, list_images
from utils.encryption import encrypt_data, decrypt_data
from utils.metrics import calculate_psnr, calculate_mse
from config import SECRET_PATH, INPUT_FOLDER, STEGO_FOLDER, OUTPUT_FOLDER, PASSWORD
import os
import argparse
from utils.getDetailsPicture import get_image_details

def run(mode="both"):
    with open(SECRET_PATH, "rb") as f:
        raw_data = f.read()
    encrypted = encrypt_data(raw_data, PASSWORD)

    if mode in ["encrypt", "both"]:
        print("[*] Starting encryption and embedding...")
        images = list_images(INPUT_FOLDER)
        get_image_details(images)
        
        for img_file in images:
            input_path = os.path.join(INPUT_FOLDER, img_file)
            img = load_image(input_path)

            try:
                stego_img = embed_data(img, encrypted)
            except ValueError as ve:
                print(f"[!] Skipping {img_file}: {ve}")
                continue

            stego_path = os.path.join(STEGO_FOLDER, f"stego_{img_file}")
            save_image(stego_path, stego_img)
            print(f"[+] Embedded: {stego_path}")

    if mode in ["decrypt", "both"]:
        print("[*] Starting extraction and decryption...")
        stego_images = list_images(STEGO_FOLDER)
        get_image_details(stego_images, status="stego")
        
        for img_file in stego_images:
            stego_path = os.path.join(STEGO_FOLDER, img_file)
            stego_loaded = load_image(stego_path)
            
            try:
                extracted = extract_data(stego_loaded)
                decrypted = decrypt_data(extracted, PASSWORD)
            except Exception as e:
                print(f"[!] Error during extraction/decryption: {e}")
                continue

            output_path = os.path.join(OUTPUT_FOLDER, f"recovered_{os.path.splitext(img_file)[0]}.txt")
            with open(output_path, "wb") as f:
                f.write(decrypted)

            psnr = calculate_psnr(stego_loaded, stego_loaded)
            mse = calculate_mse(stego_loaded, stego_loaded)
            print(f"[+] PSNR: {psnr:.2f} dB | MSE: {mse:.4f} | Saved: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="LSB Steganography with AES Encryption")
    parser.add_argument("-m", "--mode", choices=["encrypt", "decrypt", "both"], 
                        default="both", help="Mode: encrypt, decrypt, or both (default: both)")
    args = parser.parse_args()
    
    run(mode=args.mode)
