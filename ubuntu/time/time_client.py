import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ("localhost", 5000)
socket.connect((address))
print("현재 시각:", socket.recv(1024).decode())