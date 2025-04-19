from Crypto.Cipher import DES3
import base64
import os

def enkripto():

    input_file = input("Shkruaj emrin e fajllit që dëshiron të enkriptosh: ")
    output_file = input_file + ".encrypted"


    key = b'1234567890abcdef12345678'
    iv = os.urandom(8)

    cipher_encrypt = DES3.new(key, DES3.MODE_CBC, iv)

    with open(input_file, 'rb') as file:
        file_data = file.read()

    while len(file_data) % 8 != 0:
        file_data += b'\x00'

    ciphertext = cipher_encrypt.encrypt(file_data)


    iv_and_cipher = iv + ciphertext


    encoded_data = base64.b64encode(iv_and_cipher)


    with open(output_file, 'wb') as enc_file:
        enc_file.write(encoded_data)

    print(f"Fajlli u enkriptua dhe u ruajt si base64 në: {output_file}")
