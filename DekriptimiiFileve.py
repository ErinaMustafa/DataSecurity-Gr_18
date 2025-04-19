from Crypto.Cipher import DES3
import base64

key = b'1234567890abcdef12345678'

def dekripto():
    input_file = input("Shkruaj emrin e fajllit që dëshiron të dekriptosh: ")
    output_file = input_file.replace(".enc", ".decrypted")

    with open(input_file, 'rb') as enc_file:
        encoded_data = enc_file.read()

    iv_and_cipher = base64.b64decode(encoded_data)
    iv = iv_and_cipher[:8]
    ciphertext = iv_and_cipher[8:]
