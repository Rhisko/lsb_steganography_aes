import numpy as np

def calculate_psnr(original: np.ndarray, stego: np.ndarray) -> float:
    mse = calculate_mse(original, stego)
    if mse == 0:
        return float('inf')
    PIXEL_MAX = 255.0
    return 20 * np.log10(PIXEL_MAX / np.sqrt(mse))

def calculate_mse(original: np.ndarray, stego: np.ndarray) -> float:
    return np.mean((original.astype(np.float64) - stego.astype(np.float64)) ** 2)