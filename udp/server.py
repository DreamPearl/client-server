import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("127.0.0.1", 5050))

while True:
    message, addr = s.recvfrom(1024)
    print("Received message: %s" %message)