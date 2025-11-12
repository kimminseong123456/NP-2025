from socket import *
import struct

GROUP = "239.255.0.1"
PORT = 5005
BUF  = 1024

WIN_IF = "172.31.16.1" 

r = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)
r.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
r.bind(("", PORT))

mreq = struct.pack("=4s4s", inet_aton(GROUP), inet_aton(WIN_IF))
r.setsockopt(IPPROTO_IP, IP_ADD_MEMBERSHIP, mreq)

print("Ready to receive")
while True:
    data, addr = r.recvfrom(BUF)
    print(f"Received {data.decode()} from {addr}")
    r.sendto(b"ACK", addr)
