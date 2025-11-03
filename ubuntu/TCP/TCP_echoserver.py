import socket

port = 2500
BUFFSIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 재실행 시 포트 에러 방지
sock.bind(('localhost', port))
sock.listen(1)  # 연결 대기열 생성
print(f"Listening on port {port}...")

conn, addr = sock.accept()
print('Connected by', addr[0], addr[1])

while True:
    data = conn.recv(BUFFSIZE)
    if not data:
        break
    print('Received message:', data.decode())
    conn.send(data)

conn.close()
sock.close()
print("Connection closed.")
