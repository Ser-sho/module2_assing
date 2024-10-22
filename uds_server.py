import socket
import os

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
socket_path = 'my_socket'

if os.path.exists(socket_path):
    os.remove(socket_path)

sock.bind(socket_path)
sock.listen(1)

connection, _ = sock.accept()
msg = connection.recv(1024)
print(f"Server received: {msg.decode()}")
connection.close()
