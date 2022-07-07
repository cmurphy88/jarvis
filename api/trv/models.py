from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from api.db import Base


class Trv(Base):
    __tablename__ = "trv"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ip_address = Column(String(50))

    trv_routine_settings = relationship("Trv")

    # room = relationship("Room", back_populates="home")
    # home_user = relationship("HomeUser", back_populates="home")

    def __init__(self, name, ip_address, *args, **kwargs):
        self.name = name
        self.ip_address = ip_address
