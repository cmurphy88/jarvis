from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from api.db import Base


class MediaRoom(Base):
    __tablename__ = "media_room"

    id = Column(Integer, primary_key=True, autoincrement=True)
    media_id = Column(Integer, ForeignKey('media.id'))
    room_id = Column(Integer, ForeignKey('room.id'))

    medias = relationship("Media")
    rooms = relationship("Room")

    def __init__(self, media_id, room_id, *args, **kwargs):
        self.media_id = media_id
        self.room_id = room_id
