from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from api.db import Base


class RoomUserEntry(Base):
    __tablename__ = "room_user_entry"

    id = Column(Integer, primary_key=True, autoincrement=True)
    room_id = Column(Integer, ForeignKey('room.id'))
    user_id = Column(Integer, ForeignKey('users.id'))

    rooms = relationship("Room")
    users = relationship("User")

    def __init__(self, user_id, room_id, *args, **kwargs):
        self.room_id = room_id
        self.user_id = user_id

