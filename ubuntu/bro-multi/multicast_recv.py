from socket import *
import struct

GROUP = "239.255.0.1"
PORT = 5005
BUF  = 1024

WIN_IF = "172.31.16.1"  # ← Windows의 vEthernet(WSL) 실제 IP

r = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)
r.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
r.bind(("", PORT))

# ★ 멀티캐스트 가입 시 인터페이스 지정(Windows는 2번째 인자에 로컬 NIC IP를 넣는 형식이 안전)
mreq = struct.pack("=4s4s", inet_aton(GROUP), inet_aton(WIN_IF))
r.setsockopt(IPPROTO_IP, IP_ADD_MEMBERSHIP, mreq)

print("Ready to receive")
while True:
    data, addr = r.recvfrom(BUF)
    print(f"Received {data.decode()} from {addr}")
    r.sendto(b"ACK", addr)
