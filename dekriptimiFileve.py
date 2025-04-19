from Crypto.Cipher import DES3
import base64
key = b'0123456789abcdef'
def decrypt_text(encrypted_text):
    decrypted_text = ''
    cipher = DES3.new(key, DES3.MODE_ECB)
    encrypted_bytes = base64.b64decode(encrypted_text)
    
    return decrypted_text;
