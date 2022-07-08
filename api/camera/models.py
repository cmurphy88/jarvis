from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from api.db import Base


class Camera(Base):
    __tablename__ = "camera"

    id = Column(Integer, primary_key=True, autoincrement=True)
    ip_address = Column(String(50))

    # camera_rooms = relationship("RoomCamera")

    def __init__(self, ip_address, *args, **kwargs):
        self.ip_address = ip_address
