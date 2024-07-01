import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('192.2.6.100',12345))
s.listen()
conn, addr = s.accept()
data = conn.recv(1024)
conn.sendall("Hola, client".encode())

# UPD
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# s.bind(('localhost',12345))
# print("Esperando conexion")

# while True:
#     data, client_address = s.recvfrom(1024)
#     print ("Mensaje recibido:", data.decode())
#     respuesta = "Hola, client"
#     s.sendto(respuesta.encode(), client_address)