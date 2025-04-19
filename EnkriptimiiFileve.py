from Crypto.Cipher import DES3
import base64
import os

input_file = input("Shkruaj emrin e fajllit që dëshiron të enkriptosh: ")
output_file = input_file + ".enc"


key = b'1234567890abcdef12345678'
iv = os.urandom(8)


cipher_encrypt = DES3.new(key, DES3.MODE_CBC, iv)
