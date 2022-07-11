from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey, Time

from sqlalchemy.orm import relationship

from api.db import Base


class Routine(Base):
    __tablename__ = "routine"

    id = Column(Integer, primary_key=True, autoincrement=True)
    room_id = Column(Integer, ForeignKey('room.id', ondelete="CASCADE"))
    user_id = Column(Integer, ForeignKey('users.id', ondelete="CASCADE"))
    start_time = Column(Time)
    end_time = Column(Time)

    room = relationship("Room", back_populates="routine")
    users = relationship("User", back_populates="routine")
    # media_routine_settings = relationship("MediaRoutineSetting")
    # trv_routine_settings = relationship("TrvRoutineSetting")
    # light_routine_settings = relationship("LightRoutineSetting")

    def __init__(self, room_id, user_id, start_time, end_time, *args, **kwargs):
        self.room_id = room_id
        self.user_id = user_id
        self.start_time = start_time
        self.end_time = end_time

