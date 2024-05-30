import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#host = "localhost"
host = "185.179.188.156"


s.connect((host, 51111))
while True:
    out = s.recv(2048)

    s.send(b"got it" + out)
