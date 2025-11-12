import socket

port = int(input("Port No:"))    
server_ip = input("Server IP:") 
address = (server_ip, port)

BUFSIZE = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(address)

while True:
    msg = input("Message to send (quit to exit): ")
    if msg == "quit":
        break
    s.send(msg.encode())
    data = s.recv(BUFSIZE)
    print("Received message:", data.decode())

s.close()
