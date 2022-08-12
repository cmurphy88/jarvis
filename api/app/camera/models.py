from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..db import Base


class Camera(Base):
    __tablename__ = "camera"

    id = Column(Integer, primary_key=True, autoincrement=True)
    ip_address = Column(String(50))

    # camera_rooms = relationship("RoomCamera")

    def __init__(self, ip_address, *args, **kwargs):
        self.ip_address = ip_address


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
