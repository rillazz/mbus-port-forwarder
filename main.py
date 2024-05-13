import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 15228))

s.listen(4)

while True:
    c_s, addr = s.accept()
    data = c_s.recv(1024).decode("utf-8")
    print(data)
