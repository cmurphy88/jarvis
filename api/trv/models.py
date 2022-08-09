from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from api.db import Base


class Trv(Base):
    __tablename__ = "trv"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ip_address = Column(String(50))

    # trv_routine_settings = relationship("Trv")

    # room = relationship("Room", back_populates="home")
    # home_user = relationship("HomeUser", back_populates="home")

    def __init__(self, name, ip_address, *args, **kwargs):
        self.name = name
        self.ip_address = ip_address


class TrvRoom(Base):
    __tablename__ = "trv_room"

    id = Column(Integer, primary_key=True, autoincrement=True)
    trv_id = Column(Integer, ForeignKey('trv.id'))
    room_id = Column(Integer, ForeignKey('room.id'))

    trvs = relationship("Trv")
    rooms = relationship("Room")

    def __init__(self, trv_id, room_id, *args, **kwargs):
        self.trv_id = trv_id
        self.room_id = room_id


class TrvRoutineSetting(Base):
    __tablename__ = "trv_routine_setting"

    id = Column(Integer, primary_key=True, autoincrement=True)
    trv_id = Column(Integer, ForeignKey('trv.id'))
    routine_id = Column(Integer, ForeignKey('routine.id'))
    temperature = Column(Integer)
    is_active = Column(Boolean)

    device = relationship("Trv")
    routines = relationship("Routine")

    def __init__(self, trv_id, routine_id, temperature, is_active, *args, **kwargs):
        self.trv_id = trv_id
        self.routine_id = routine_id
        self.temperature = temperature
        self.is_active = is_active
