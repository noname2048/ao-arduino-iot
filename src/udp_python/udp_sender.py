import socket
import time

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.connect(("iot.noname2048.com", 8050))

    i = 0
    while True:
        time.sleep(5)

        data = f"HI {i}".encode()
        print(data)
        sock.sendall(data)

        i += 1
