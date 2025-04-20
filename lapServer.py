import socket
#krijimi i nje serveri socket
server_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#konffigurimi i ip dhe port
server_ip = "192.168.1.43"
server_port = 12345

#lejimi i qasjes se klientit ne server 
server_socket.bind((server_ip, server_port))
server_socket.listen(1)

#pritja e klientit per tu qasur
print(f"Serveri duke pritur lidhje ne portin {server_port} ...")

# pranimi i qasjes se klientit
conn, addr = server_socket.accept()
print(f"Lidhur nga: {addr}")

# pranimi i mesazhit nga klienti
while True:
    data = conn.recv(1024)
    if not data:
        break;
    print("Mesazhi i pranuar:", data.decode())

# mbyllja e lidhjes
conn.close()
