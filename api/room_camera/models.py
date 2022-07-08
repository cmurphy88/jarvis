from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from api.db import Base


class CameraRoom(Base):
    __tablename__ = "camera_room"

    id = Column(Integer, primary_key=True, autoincrement=True)
    camera_id = Column(Integer, ForeignKey('camera.id'))
    room_id = Column(Integer, ForeignKey('room.id'))

    cameras = relationship("Camera")
    rooms = relationship("Room")

    def __init__(self, camera_id, room_id, *args, **kwargs):
        self.camera_id = camera_id
        self.room_id = room_id
