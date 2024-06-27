
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect (('127.0.0.1', 12345))
s.send("Hola, servidor".encode())
response = s.recv(1024).decode()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost',12345))
s.listen()
print("Esperando conexion")
conn, addr = s.accept()
data = conn.recv(1024)
conn.sendall("Message for client".encode())
