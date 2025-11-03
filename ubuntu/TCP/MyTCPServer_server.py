import MyTCPServer as mt
import sys

port = 2500

if len(sys.argv) > 1:
    port = int(sys.argv[1])

sock = mt.TCPServer(port)
c, addr = sock.Accept()

while True:
    print('Connected by', addr[0], addr[1]) 
    data = c.recv(1024)
    if not data:
        break
    print('Received message:', data.decode())
    c.send(data)

c.close()
print(" 연결 종료")
