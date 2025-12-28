# 🔒 LSB Steganography + AES Encryption

> A secure Python project to hide encrypted messages inside digital images using **Least Significant Bit (LSB)** steganography and **AES-256 encryption** with CBC mode. Built with cryptographic best practices (random IV, password-based key derivation).

---

## 📂 Project Structure

```
lsb_steganography_aes/
├── main.py                  # CLI pipeline for embed + extract
├── config.py                # User config (e.g. password)
├── requirements.txt         # Project dependencies
├── README.md                # This file
│
├── utils/                   # Modular core logic
│   ├── encryption.py        # AES encrypt/decrypt with random IV
│   ├── steganography.py     # LSB embed/extract logic
│   ├── image_io.py          # Image loader/saver
│   └── metrics.py           # PSNR & MSE calculation
│
├── samples/
│   ├── input/               # Original input images (.png)
│   ├── secret/              # Secret file to embed (e.g. .txt)
│   └── stego/               # Output images with embedded data
│
└── outputs/                 # Extracted secret messages
```

---

## ✅ Features

- 🔐 AES-256 encryption (CBC mode) with random IV & PBKDF2 password key
- 🧠 LSB-based steganography (bit-level manipulation)
- 🔍 Evaluation metrics: PSNR, MSE
- ⚠️ Rejects images too small for message size
- 💡 Supports batch processing of images in `samples/input/`

---

## ⚙️ Installation

```bash
python3 -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

---

## 🚀 How to Use

1. Place PNG cover images into: `samples/input/`
2. Place a secret message file: `samples/secret/message.txt`
3. Set your password in `config.py`:

```python
PASSWORD = "MyStrongPassword123!"
```

4. Run the tool:

```bash
python main.py
```

✅ Stego images → `samples/stego/`
✅ Recovered messages → `outputs/`

---

## 📊 Output Sample (printed per image)

```
[*] Processing image1.png...
    → PSNR: 47.25 dB | MSE: 0.76 | Saved: outputs/recovered_image1.txt
```

---

## 📌 Limitations

- Works best with lossless formats: **PNG** or **BMP**
- Avoid using JPEG due to lossy compression corrupting LSB bits
- Each image must be large enough to embed your encrypted message

---

---

## 👨‍💻 Author

- Developed by Risko
- Contributions, issues, and stars are welcome on GitHub ⭐

---

## 📄 License

This project is licensed under the MIT License.
