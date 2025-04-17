from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

plaintext = input("Shkruaj tekstin që dëshiron të enkriptosh: ")

key = DES3.adjust_key_parity(get_random_bytes(24))

iv = get_random_bytes(8)

cipher_encrypt = DES3.new(key, DES3.MODE_CBC, iv)


ciphertext = cipher_encrypt.encrypt(pad(plaintext.encode(), DES3.block_size))

print("\nTeksti i enkriptuar (hex):", ciphertext.hex())
