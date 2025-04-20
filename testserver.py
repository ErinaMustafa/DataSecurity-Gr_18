from enkriptimiTekstit import encrypt_text
from dekriptimiTekstit import decrypt_text
import socket



server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('192.168.1.43', 12345))
server_socket.listen(1)

print("Serveri duke pritur...")

conn, addr = server_socket.accept()
print(f"U lidh klienti: {addr}")


while True:
    data = conn.recv(1024)
    decrypted_message = decrypt_text(data)
    print("Mesazhi i pranuar nga klienti:", decrypted_message)

    if decrypted_message.lower() == "stop":
        print("Klienti dergoi 'stop'. Po mbyllim lidhjen...")
        break

    response = input("Shkruaj pergjigjen per klientin: ")
    encrypted_response = encrypt_text(response)
    conn.send(encrypted_response)

    if response.lower() == "stop":
        print("Derguam 'stop'. Po mbyllim lidhjen...")
        break

conn.close()
server_socket.close()