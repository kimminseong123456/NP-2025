import socket
sock = socket.create_connection(('localhost',2500))

message = "Clinet Message"
print('sending {}', format(message))
sock.sendall(message.encode())

data = sock.recv(1024)
print('received {}', format (data.decode()))
print('closing socket')
sock.close()