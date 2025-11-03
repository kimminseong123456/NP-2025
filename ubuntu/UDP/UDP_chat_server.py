import socket

port = 2500
BUFFSIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("", port))
print("UDP Chat Server started on port", port)

while True:
    print("<- ", end="")
    data, addr = sock.recvfrom(BUFFSIZE)
    print(data.decode())

    resp = input("-> ")
    sock.sendto(resp.encode(), addr)
