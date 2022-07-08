from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from api.db import Base


class RoomAlert(Base):
    __tablename__ = "room_alert"

    id = Column(Integer, primary_key=True, autoincrement=True)
    room_id = Column(Integer, ForeignKey('room.id'))
    message = Column(Text)

    rooms = relationship("Room")

    def __init__(self, room_id, message, *args, **kwargs):
        self.room_id = room_id
        self.message = message
