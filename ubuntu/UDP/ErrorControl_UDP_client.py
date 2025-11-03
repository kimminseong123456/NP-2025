import socket
import time

SERVER = "localhost"   
PORT = 2500
BUFFER = 1024

MAX_TRIES = 10
INIT_TIMEOUT = 0.1     
MAX_TIMEOUT = 2.0     

msg = "Hello message"

c_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
c_sock.connect((SERVER, PORT))

for attempt in range(1, MAX_TRIES + 1):
    delay = INIT_TIMEOUT             
    c_sock.send(msg.encode())

    while True:
        print(f"[try {attempt}] Waiting up to {delay:.3f}s for a reply...")
        c_sock.settimeout(delay)
        try:
            data = c_sock.recv(BUFFER)       
        except socket.timeout:
            delay *= 2                     
            if delay > MAX_TIMEOUT:         
                print("  timeout -> give up this try")
                break
           
        else:
            print("Response:", data.decode())
            c_sock.close()
            raise SystemExit(0)

print("No response after all tries. Exiting.")
c_sock.close()
