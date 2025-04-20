from enkriptimiTekstit import encrypt_text
from dekriptimiTekstit import decrypt_text

import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('192.168.1.43', 12345))

while True:
    message = input("Shkruaj mesazhin: ")
    encrypted_message = encrypt_text(message)
    client_socket.send(encrypted_message)

    while True:
        message = input("Shkruaj mesazhin: ")
        encrypted_message = encrypt_text(message)
        client_socket.send(encrypted_message)

        if message.lower() == "stop":
            print("Derguam komandën 'stop'. Po largohemi...")
            break
            data = client_socket.recv(1024)
            decrypted_response = decrypt_text(data)
            print("Pergjigje nga serveri:", decrypted_response)

            if decrypted_response.lower() == "stop":
                print("Serveri dergoi 'stop'. Po largohemi...")
                break

        client_socket.close()