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
