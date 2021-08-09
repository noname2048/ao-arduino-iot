from typing import List, Optional
from pydantic import BaseModel

import datetime


class SensorValueBase(BaseModel):
    device_id: int
    time: datetime.datetime
    temperature: float
    humidity: float


class SensorValueCreate(SensorValueBase):
    pass


class SensorValue(SensorValueBase):
    id: int

    class Config:
        orm_mode = True


class DeviceBase(BaseModel):
    modelname: str
    pincode: str

    created_at: Optional[datetime.datetime]
    updated_at: Optional[datetime.datetime]


class DeviceCreate(DeviceBase):
    pass


class Device(DeviceBase):
    id: int
    sensorvalue_set: List[SensorValue]
