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


