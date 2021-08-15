import socket
import re
import pathlib
import sys
from datetime import datetime, timedelta, timezone
from typing import List

print(pathlib.Path(__file__).parent.parent / "remote_db")
sys.path.append(pathlib.Path(__file__).parent.parent / "remote_db")
print(sys.path)
from remote_db.models import SensorValue
from remote_db import Base, SessionLocal


data_comp = re.compile(r"T(?P<TEMP>[-0-9]+.\d+),H(?P<HUMID>[-0-9]+.\d+)")
def str2info(s: str) -> List[float]:
    result = data_comp.search(s)
    if result != None:
        result_dict = result.groupdict()
        temp = float(result_dict.get("TEMP"))
        humid = float(result_dict.get("HUMID"))
        return temp, humid
    else:
        return None, None
    
t = socket.gethostbyname(socket.gethostname())
host: str = t
# host: str = "192.168.35.2"
port: int = 8050

def now(format: str = "%H:%M:%S") -> str:
    ret = datetime.now(tz=timezone(timedelta(hours=9)))
    return ret.strftime(format)
    
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    try:
        print("UDP Start")
        sock.bind((host, port))

        while True:
            data, addr = sock.recvfrom(1024)

            temp, humi = str2info(data.decode())
            if temp != None:
                with SessionLocal() as session:
                    sensor_value = SensorValue(temperature=temp, humidity=humi, device_id=2)
                    session.add(sensor_value)
                    session.commit()

    except KeyboardInterrupt as e:
        print("\nUDP Done")