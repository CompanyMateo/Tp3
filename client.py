# import socket
# s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# s.connect (('localhost', 12345))
# s.sendto("Hola, servidor".decode())
# response, server = s.recvfrom(1024)
# print("Respuesta del servidor:", response.decode())

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.connect(('localhost', 12345))
s.send("Hola, servidor".encode())
response = s.recv(1024).decode()
print(response)
