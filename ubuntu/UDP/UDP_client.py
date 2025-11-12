import socket

BUFFSIZE = 1024
PORT = 2500

SERVER_IP = "172.31.16.1"   
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input("Message (quit to exit): ")

    if msg == "quit":
        break

    sock.sendto(msg.encode(), (SERVER_IP, PORT))
    data, addr = sock.recvfrom(BUFFSIZE)

    print("Server says:", data.decode())
