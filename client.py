import socket
#TCP
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('192.2.6.101', 12345))
s.send("Hola, servidor".encode())
response = s.recv(1024).decode()
print(response)

# UPD
# s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# s.connect (('localhost', 12345))
# s.sendto("Hola, servidor".encode())
# response = s.recv(1024).decode()
# print("Respuesta del servidor:", response.decode())
