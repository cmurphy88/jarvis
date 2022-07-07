from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from api.db import Base


class LightRoutineSetting(Base):
    __tablename__ = "light_routine_settings"

    id = Column(Integer, primary_key=True, autoincrement=True)
    light_id = Column(Integer, ForeignKey('light.id'))
    routine_id = Column(Integer, ForeignKey('routine.id'))
    media_url = Column(String(250))
    is_active = Column(Boolean)

    lights = relationship("light")
    routines = relationship("Routine")

    def __init__(self, light_id, routine_id, media_url, is_active, *args, **kwargs):
        self.light_id = light_id
        self.routine_id = routine_id
        self.media_url = media_url
        self.is_active = is_active
