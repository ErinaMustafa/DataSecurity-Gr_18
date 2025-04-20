from enkriptimiTekstit import encrypt_text
from dekriptimiTekstit import decrypt_text

import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('192.168.1.43', 12345))

while True:
    message = input("Shkruaj mesazhin: ")
    encrypted_message = encrypt_text(message)
    client_socket.send(encrypted_message)