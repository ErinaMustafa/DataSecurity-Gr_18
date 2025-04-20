from enkriptimiTekstit import encrypt_text
from dekriptimiTekstit import decrypt_text
import socket



server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('192.168.1.43', 12345))
server_socket.listen(1)

print("Serveri duke pritur...")

conn, addr = server_socket.accept()
print(f"U lidh klienti: {addr}")
