from Crypto.Cipher import DES3
import base64

key = b'0123456789abcdef'


def encrypt_text(plain_text):
    encrypted_text = ''
    cipher = DES3.new(key, DES3.MODE_ECB)

    # Padding për shumëfish të 8 bytes
    while len(plain_text) % 8 != 0:
        plain_text += '\0'

    encrypted_bytes = cipher.encrypt(plain_text.encode('utf-8'))
    encrypted_text = base64.b64encode(encrypted_bytes).decode('utf-8')
    return encrypted_text;




