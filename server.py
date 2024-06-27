
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('localhost',12345))
print("Esperando conexion")

while True:
    data, client_address = s.recvfrom(1024)
    print ("Mensaje recibido:", data.decode())
    respuesta = "Hola, client"
    s.sendto(respuesta.encode(), client_address)