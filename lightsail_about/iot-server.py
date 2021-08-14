import socket
from datetime import datetime, timedelta, timezone
from typing import List

from sqlalchemy.orm import Session

import sys
sys.path.append("../sql_about")
from ale.models import Base, SensorValue
from ale.database import SessionLocal, engine

import re

comp = re.compile(r"T(?P<TEMP>[-0-9]+.\d+),H(?P<HUMID>[-0-9]+.\d+)")
def str2info(s: str) -> List[float]:
    result = comp.search(s)
    if result != None:
        result_dict = result.groupdict()
        temp = float(result_dict.get("TEMP"))
        humid = float(result_dict.get("HUMID"))
        return temp, humid
    else:
        return None, None

host: str = "iot.noname2048.com"
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
