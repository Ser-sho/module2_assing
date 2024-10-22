import socket
import time

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
time.sleep(1)  # Ensure server is ready
sock.connect('my_socket')
sock.sendall(b'Hello from client!')
sock.close()
