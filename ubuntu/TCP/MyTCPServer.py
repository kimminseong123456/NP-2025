class TCPServer:
    def __init__(self, port):
        import socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind(('', port))
        self.sock.listen(5)
        print(f"Server listening on port {port}")

    def Accept(self):
        self.c_sock, self.c_addr = self.sock.accept()
        print(f"Connected by {self.c_addr}")
        return self.c_sock, self.c_addr


if __name__ == "__main__":
    server = TCPServer(2500)
    c, addr = server.Accept()

    while True:
        data = c.recv(1024)
        if not data:
            print("클라이언트 연결 종료됨")
            break

        print("수신 메시지:", data.decode())

        msg = "Hello Client"
        c.send(msg.encode())

    c.close()
    print("서버 종료")
