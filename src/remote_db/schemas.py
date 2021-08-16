from typing import List, Optional, Any
from pydantic import BaseModel

from datetime import datetime


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

    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()


class DeviceCreate(DeviceBase):
    pass


class Device(DeviceBase):
    id: int
    sensorvalue_set: List[SensorValue] = []

    class Config:
        orm_mode = True
