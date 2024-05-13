import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("185.179.189.222", 15145))

s.send(b"Hello!\n")
