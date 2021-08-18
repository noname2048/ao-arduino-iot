from typing import List, Optional, Any
from pydantic import BaseModel, validator

from datetime import datetime
import datetime as D

KST = D.timezone(D.timedelta(hours=9))


class SensorValueBase(BaseModel):
    device_id: int
    time: datetime
    temperature: float
    humidity: float


class SensorValueCreate(SensorValueBase):
    pass


class SensorValue(SensorValueBase):
    id: int

    class Config:
        orm_mode = True


class DeviceBase(BaseModel):
    modelname: str = "arduino mega"
    pincode: int = 2

    created_at: datetime = datetime.now(tz=KST)
    updated_at: datetime = datetime.now(tz=KST)


class DeviceCreate(DeviceBase):
    pass


class Device(DeviceBase):
    id: int
    sensorvalue_set: List[SensorValue] = []

    class Config:
        orm_mode = True
