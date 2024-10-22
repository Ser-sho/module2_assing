import socket

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind(('0.0.0.0', 12345))
server_sock.listen(1)

print("Server is listening...")

connection, _ = server_sock.accept()
msg = connection.recv(1024)
print(f"Server received: {msg.decode()}")
connection.close()
