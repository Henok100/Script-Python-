import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1456))

while True:
    msg = s.recv(1456)
    print(msg)
    print()
