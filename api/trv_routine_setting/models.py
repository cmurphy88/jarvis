from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from api.db import Base


class TrvRoutineSetting(Base):
    __tablename__ = "trv_routine_settings"

    id = Column(Integer, primary_key=True, autoincrement=True)
    trv_id = Column(Integer, ForeignKey('trv.id'))
    routine_id = Column(Integer, ForeignKey('routine.id'))
    media_url = Column(String(250))
    is_active = Column(Boolean)

    trv = relationship("Trv")
    routines = relationship("Routine")

    def __init__(self, trv_id, routine_id, media_url, is_active, *args, **kwargs):
        self.trv_id = trv_id
        self.routine_id = routine_id
        self.media_url = media_url
        self.is_active = is_active
