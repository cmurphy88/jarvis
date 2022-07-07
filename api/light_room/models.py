from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from api.db import Base


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
