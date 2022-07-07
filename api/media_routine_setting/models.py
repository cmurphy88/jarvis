from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from api.db import Base


class MediaRoutineSetting(Base):
    __tablename__ = "media_routine_settings"

    id = Column(Integer, primary_key=True, autoincrement=True)
    media_id = Column(Integer, ForeignKey('media.id'))
    routine_id = Column(Integer, ForeignKey('routine.id'))
    media_url = Column(String(250))
    is_active = Column(Boolean)

    medias = relationship("Media")
    routines = relationship("Routine")

    def __init__(self, media_id, routine_id, media_url, is_active, *args, **kwargs):
        self.media_id = media_id
        self.routine_id = routine_id
        self.media_url = media_url
        self.is_active = is_active
