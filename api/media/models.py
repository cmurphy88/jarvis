from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from api.db import Base


class Media(Base):
    __tablename__ = "media"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ip_address = Column(String(50))
    is_playing = Column(Boolean)

    # media_routine_setting = relationship("MediaRoutineSetting")

    def __init__(self, name, ip_address, is_playing, *args, **kwargs):
        self.name = name
        self.ip_address = ip_address
        self.is_playing = is_playing


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


class MediaRoutineSetting(Base):
    __tablename__ = "media_routine_setting"

    id = Column(Integer, primary_key=True, autoincrement=True)
    media_id = Column(Integer, ForeignKey('media.id'))
    routine_id = Column(Integer, ForeignKey('routine.id'))
    media_url = Column(String(250))
    is_active = Column(Boolean)

    device = relationship("Media")
    routines = relationship("Routine")

    def __init__(self, media_id, routine_id, media_url, is_active, *args, **kwargs):
        self.media_id = media_id
        self.routine_id = routine_id
        self.media_url = media_url
        self.is_active = is_active

