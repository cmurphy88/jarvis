from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from api.db import Base


class Light(Base):
    __tablename__ = "light"

    id = Column(Integer, primary_key=True, autoincrement=True)
    ip_address = Column(String(50))

    def __init__(self, ip_address, *args, **kwargs):
        self.ip_address = ip_address


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
    __tablename__ = "light_routine_settings"

    id = Column(Integer, primary_key=True, autoincrement=True)
    light_id = Column(Integer, ForeignKey('light.id'))
    routine_id = Column(Integer, ForeignKey('routine.id'))
    media_url = Column(String(250))
    is_active = Column(Boolean)

    lights = relationship("light")
    routines = relationship("Routine")

    def __init__(self, light_id, routine_id, media_url, is_active, *args, **kwargs):
        self.light_id = light_id
        self.routine_id = routine_id
        self.media_url = media_url
        self.is_active = is_active
