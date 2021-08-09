from sqlalchemy.orm import Session
from . import models, schemas


def get_device(db: Session, device_id: int):
    return db.query(models.Device).filter(models.Device.id == device_id).first()


def create_device(db: Session, device: schemas.DeviceCreate):
    db_device = models.Device(modelname=device.modelname, pincode=device.pincode)
    db.add(db_device)
    db.commit()
    db.refresh(db_device)
    return db_device
