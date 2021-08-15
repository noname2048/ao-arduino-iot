import socket
import datetime

host: str = "192.168.35.2"
port: int = 8050

def now() -> str:
    return datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=9))).strftime("%H:%M:%S")

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    try:
        sock.bind((host, port))
        print("UDP Start")

        while True:
            data, addr = sock.recvfrom(1024)
            
            print(f"[{now()}] {data.decode()}")

    except KeyboardInterrupt as e:
        print("UDP Done")