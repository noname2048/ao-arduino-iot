import sys
import os
sys.path.append("..")

from typing import List, Any, Optional
from fastapi import Depends, FastAPI, HTTPException, WebSocket
from sqlalchemy.orm import Session
from remote_db import crud, models, schemas
from remote_db.database import SessionLocal, engine
import uvicorn
from pydantic import BaseModel
import asyncio
import json

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

@app.get("/")
async def home(item: Item):
    return {"messagee": "HI"}

# list device
@app.get("/devices/", response_model=List[schemas.Device])
def list_device(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    devices = crud.list_device(db, skip=skip, limit=limit)
    return devices

# create device
@app.post("/devices/", response_model=schemas.Device)
def create_device(device: schemas.DeviceCreate, db: Session = Depends(get_db)):
    db_device = crud.retrieve_device(db, pincode=device.pincode)
    if db_device:
        raise HTTPException(status_code=400, detail="Device that has pincode already")
    return crud.create_device(db=db, device=device)

# retrieve device
@app.get("/devices/{device_pincode}/", response_model=schemas.Device)
def retrieve_device(device_pincode: int, db: Session = Depends(get_db)):
    db_device = crud.retrieve_device(db, pincode=device_pincode)
    if db_device is None:
        raise HTTPException(status_code=404, detail="Devices not found")
    return db_device

@app.get("/devices/{device_pincode}/sensorvalue/", response_model=List[schemas.SensorValue])
def list_device_sensorvalues(device_pincode: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_device = crud.retrieve_device(db, pincode=device_pincode)
    if db_device is None:
        raise HTTPException(status_code=404, detail="Devices not found")
    db_sensorvalue = crud.list_device_sensorvalue(db, device_pincode, skip, limit)
    return db_sensorvalue


@app.websocket("/ws")
async def websocket_temperature(websocket: WebSocket, db: Session = Depends(get_db)):
    await websocket.accept()
    while True:
        await asyncio.sleep(10)
        db_sensorvalue = crud.last_device_sensorvalue(pincode=2, db=db)
        await websocket.send("")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
