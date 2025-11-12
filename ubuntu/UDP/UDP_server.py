import socket

PORT = 2500
BUFFSIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(("0.0.0.0", PORT))
print(f"UDP Server started on port {PORT}...")

while True:
    data, addr = sock.recvfrom(BUFFSIZE)
    print(f"Received from {addr}: {data.decode()}")
    
    
    sock.sendto(data, addr)
