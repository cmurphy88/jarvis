from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from ..db import Base


class Light(Base):
    __tablename__ = "light"

    id = Column(Integer, primary_key=True, autoincrement=True)
    ip_address = Column(String(50))
    name = Column(String(50))

    def __init__(self, ip_address, name, *args, **kwargs):
        self.ip_address = ip_address
        self.name = name


class LightRoom(Base):
    __tablename__ = "light_room"

    id = Column(Integer, primary_key=True, autoincrement=True)
    light_id = Column(Integer, ForeignKey('light.id'))
    room_id = Column(Integer, ForeignKey('room.id'))

    lights = relationship("Light")
    rooms = relationship("Room")

    def __init__(self, light_id, room_id, *args, **kwargs):
        self.light_id = light_id
        self.room_id = room_id


class LightRoutineSetting(Base):
    __tablename__ = "light_routine_setting"

    id = Column(Integer, primary_key=True, autoincrement=True)
    light_id = Column(Integer, ForeignKey('light.id'))
    routine_id = Column(Integer, ForeignKey('routine.id'))
    brightness = Column(Integer)
    is_active = Column(Boolean)

    device = relationship("Light")
    routines = relationship("Routine")

    def __init__(self, light_id, brightness, is_active, *args, **kwargs):
        self.light_id = light_id
        self.brightness = brightness
        self.is_active = is_active
