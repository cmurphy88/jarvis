from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from api.db import Base


class Light(Base):
    __tablename__ = "light"

    id = Column(Integer, primary_key=True, autoincrement=True)
    ip_address = Column(String(50))

    def __init__(self, ip_address, *args, **kwargs):
        self.ip_address = ip_address
