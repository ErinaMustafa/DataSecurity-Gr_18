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

    cipher_decrypt = DES3.new(key, DES3.MODE_CBC, iv)
    decrypted_data = cipher_decrypt.decrypt(ciphertext)
    decrypted_data = decrypted_data.rstrip(b'\x00')

    with open(output_file, 'wb') as dec_file:
        dec_file.write(decrypted_data)

    print(f"Fajlli u dekriptua me sukses dhe u ruajt si: {output_file}")

