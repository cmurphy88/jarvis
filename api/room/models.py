from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey
from sqlalchemy.orm import relationship

from api.db import Base


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
