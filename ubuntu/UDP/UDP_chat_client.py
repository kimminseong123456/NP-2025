import socket

BUFFSIZE = 1024
SERVER = 'localhost'
PORT = 2500

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input("-> ")
    sock.sendto(msg.encode(), (SERVER, PORT))

    print("<- ", end="")
    data, addr = sock.recvfrom(BUFFSIZE)
    print(data.decode())
