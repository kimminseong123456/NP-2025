import socket
import random

PORT = 2500
BUFFER = 1024

s_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s_sock.bind(("", PORT))
print("Listening...")

while True:
    data, addr = s_sock.recvfrom(BUFFER)

    if random.randint(1, 10) < 4:
        print("Packet from {} lost!!!".format(addr))
        continue  

    print("Message is {!r} from {}".format(data.decode(), addr))  
    s_sock.sendto("ACK".encode(), addr) 
