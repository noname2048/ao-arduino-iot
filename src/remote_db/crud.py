from sqlalchemy.orm import Session
from . import models, schemas


def list_device(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Device).offset(skip).limit(limit).all()


def create_device(db: Session, device: schemas.DeviceCreate):
    db_device = models.Device(modelname=device.modelname, pincode=device.pincode)
    db.add(db_device)
    db.commit()
    db.refresh(db_device)
    return db_device


def retrieve_device(db: Session, pincode: int):
    return db.query(models.Device).filter(models.Device.pincode == pincode).first()


def list_device_sensorvalue(db: Session, pincode: int, skip: int = 0, limit: int = 100):
    db_device = db.query(models.Device).filter(models.Device.pincode == pincode).first()
    return (
        db.query(models.SensorValue)
        .filter(models.SensorValue.device == db_device)
        .offset(skip)
        .limit(limit)
        .all()
    )
