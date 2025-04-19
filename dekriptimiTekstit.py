from Crypto.Cipher import DES3
import base64
key = b'0123456789abcdef'
def decrypt_text(encrypted_text):
    decrypted_text = ''
    cipher = DES3.new(key, DES3.MODE_ECB)
    encrypted_bytes = base64.b64decode(encrypted_text)
    decrypted_bytes = cipher.decrypt(encrypted_bytes)
    decrypted_text = decrypted_bytes.rstrip(b'\x00').decode('utf-8')
    return decrypted_text;
