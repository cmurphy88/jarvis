from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from api.db import Base


class RoomUserHierarchy(Base):
    __tablename__ = "room_user_hierarchy"

    id = Column(Integer, primary_key=True, autoincrement=True)
    room_id = Column(Integer, ForeignKey('room.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    user_order = Column(Integer, unique=True)

    rooms = relationship("Room")
    users = relationship("User")

    def __init__(self, camera_id, room_id, user_order, *args, **kwargs):
        self.camera_id = camera_id
        self.room_id = room_id
        self.user_order = user_order
