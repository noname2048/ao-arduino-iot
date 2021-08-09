from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Numeric
from sqlalchemy.orm import relationship
from datetime import datetime

from .database import Base


class Device(Base):
    __tablename__ = "devices"

    id = Column(Integer, primary_key=True, index=True)
    modelname = Column(String(30), nullable=False)
    pincode = Column(Integer, unique=True, nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.now, nullable=False)
    updated_at = Column(
        DateTime(timezone=True),
        onupdate=datetime.now,
        default=datetime.now,
        nullable=False,
    )

    sensorvalue_set = relationship("SensorValue", back_populates="device")


class SensorValue(Base):
    __tablename__ = "values"

    id = Column(Integer, primary_key=True, index=True)
    time = Column(DateTime(timezone=True), default=datetime.now, nullable=False)
    temperature = Column(Numeric, nullable=False)
    humidity = Column(Numeric, nullable=False)

    device_id = Column(Integer, ForeignKey("devices.id"), nullable=False)
    device = relationship("Device", back_populates="sensorvalue_set")
