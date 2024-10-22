import socket

server_ip = '192.168.8.203'
client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.connect((server_ip, 12345))
client_sock.sendall(b'Hello from client!')
client_sock.close()
