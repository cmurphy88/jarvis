from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from ..db import Base


class Room(Base):
    __tablename__ = "room"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    home_id = Column(Integer, ForeignKey('home.id', ondelete="CASCADE"))

    home = relationship("Home", back_populates="room")
    routine = relationship("Routine", back_populates="room")
    # room_alert = relationship("RoomAlert")
    # room_user_entry = relationship("RoomUserEntry")

    def __init__(self, name, home_id, *args, **kwargs):
        self.name = name
        self.home_id = home_id


class RoomAlert(Base):
    __tablename__ = "room_alert"

    id = Column(Integer, primary_key=True, autoincrement=True)
    room_id = Column(Integer, ForeignKey('room.id'))
    message = Column(Text)

    rooms = relationship("Room")

    def __init__(self, room_id, message, *args, **kwargs):
        self.room_id = room_id
        self.message = message


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
