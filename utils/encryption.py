
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2

def derive_key(password: bytes, salt: bytes) -> bytes:
    return PBKDF2(password, salt, dkLen=32, count=1000000)

def encrypt_data(data: bytes, password: str) -> bytes:
    salt = get_random_bytes(16)  # for key derivation
    key = derive_key(password.encode(), salt)
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(data, AES.block_size))
    return salt + iv + ciphertext  # total: 16 (salt) + 16 (IV) + ciphertext

def decrypt_data(data: bytes, password: str) -> bytes:
    salt = data[:16]
    iv = data[16:32]
    ciphertext = data[32:]
    key = derive_key(password.encode(), salt)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(ciphertext), AES.block_size)

