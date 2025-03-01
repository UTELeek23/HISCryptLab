from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def decrypt_aes(ciphertext, key):
    cipher = AES.new(key.encode(), AES.MODE_ECB)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return plaintext.decode()