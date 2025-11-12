from socket import *
import struct

GROUP = "239.255.0.1"
PORT = 5005
TTL = 1

WSL_IP = "172.31.18.175"  

s = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)
s.settimeout(0.5)
s.setsockopt(IPPROTO_IP, IP_MULTICAST_TTL, struct.pack('@i', TTL))
s.setsockopt(IPPROTO_IP, IP_MULTICAST_LOOP, 0)  

s.setsockopt(IPPROTO_IP, IP_MULTICAST_IF, inet_aton(WSL_IP))

while True:
    msg = input("Your message: ")
    s.sendto(msg.encode(), (GROUP, PORT))


