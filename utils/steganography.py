import numpy as np

def embed_data(image: np.ndarray, data: bytes) -> np.ndarray:
    flat_img = image.flatten()
    length = len(data)
    length_bytes = length.to_bytes(4, byteorder='big')
    full_data = length_bytes + data
    bit_data = ''.join(f'{byte:08b}' for byte in full_data)

    if len(bit_data) > len(flat_img):
        raise ValueError("Data too large for this image.")

    for i in range(len(bit_data)):
        flat_img[i] = (flat_img[i] & 0xFE) | int(bit_data[i])

    return flat_img.reshape(image.shape)

def extract_data(image: np.ndarray) -> bytes:
    flat_img = image.flatten()
    if len(flat_img) < 32:
        raise ValueError("Image too small to contain length header.")

    length_bits = [str(flat_img[i] & 1) for i in range(32)]
    length = int(''.join(length_bits), 2)
    total_bits = 32 + length * 8

    if total_bits > len(flat_img):
        raise ValueError("Declared data length exceeds image capacity.")

    data_bits = [str(flat_img[i] & 1) for i in range(32, total_bits)]
    byte_data = [int(''.join(data_bits[i:i+8]), 2) for i in range(0, len(data_bits), 8)]
    return bytes(byte_data)
