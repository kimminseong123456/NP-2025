import socket

class UDPClient:
    def __init__(self, server_ip='localhost', port=2500, bufsize=1024):
        self.server_ip = server_ip
        self.port = port
        self.bufsize = bufsize
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send_message(self, message):
        """서버로 메시지 전송 및 응답 수신"""
        self.sock.sendto(message.encode(), (self.server_ip, self.port))
        data, _ = self.sock.recvfrom(self.bufsize)
        print("Server says:", data.decode())

    def run(self):
        """사용자 입력 기반 통신"""
        while True:
            msg = input("Enter message (or 'quit' to exit): ")
            if msg.lower() == 'quit':
                print("Client shutting down.")
                break
            self.send_message(msg)

if __name__ == "__main__":
        UDPClient(server_ip="172.31.18.175").run()