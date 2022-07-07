from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from api.db import Base


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
