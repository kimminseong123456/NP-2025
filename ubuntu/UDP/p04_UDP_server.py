import socket

class UDPServer:
    def __init__(self, host='', port=2500, bufsize=1024):
        self.host = host
        self.port = port
        self.bufsize = bufsize
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((self.host, self.port))
        print(f"UDP Server started on port {self.port}")

    def start(self):
        """서버 실행"""
        while True:
            data, addr = self.sock.recvfrom(self.bufsize)
            message = data.decode()
            print(f"Received from {addr}: {message}")
            self.sock.sendto(data, addr)
            print(f"Echoed back to {addr}")

if __name__ == "__main__":
    server = UDPServer(port=2500)
    server.start()
