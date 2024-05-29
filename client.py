import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("localhost", 52222))

while True:
    i = input()
    s.send(i.encode())
    print(s.recv(2048).decode("utf-8"))
