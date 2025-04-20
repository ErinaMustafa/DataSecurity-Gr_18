import socket


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server_ip = '192.168.1.43'
server_port = 12345

client_socket.connect((server_ip, server_port))

message = input("Shkruaj mesazhin qe do dergosh: ")
client_socket.send(message.encode())