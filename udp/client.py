import socket

MESSAGE = b"Hello, Server!"
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(MESSAGE, ("127.0.0.1", 5050))