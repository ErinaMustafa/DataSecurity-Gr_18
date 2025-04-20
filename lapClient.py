import socket


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server_ip = '192.168.1.43'  # IP e kompjuterit ku është serveri
server_port = 12345         # Duhet të jetë i njëjtë me atë të serverit

try:
    # 3. Lidhja me serverin
    client_socket.connect((server_ip, server_port))
    print(f" U lidh me serverin {server_ip}:{server_port}")

    while True:
        # 4. Marrja e mesazhit nga përdoruesi
        message = input("Shkruaj mesazhin (ose 'dalje' për të dalë): ")

        if message.lower() == 'dalje':
            print("[x] Po e mbyllim lidhjen.")
            break

        # 5. Dërgimi i mesazhit te serveri
        client_socket.send(message.encode())

        # 6. Pritja e përgjigjes nga serveri
        response = client_socket.recv(1024).decode()
        print(f" Pergjigje nga serveri: {response}")

except Exception as e:
    print(f"Ndodhi nje gabim: {str(e)}")

