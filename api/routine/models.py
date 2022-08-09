from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey, Time, TIMESTAMP

from sqlalchemy.orm import relationship

from api.db import Base


class Routine(Base):
    __tablename__ = "routine"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    room_id = Column(Integer, ForeignKey('room.id', ondelete="CASCADE"))
    user_id = Column(Integer, ForeignKey('users.id', ondelete="CASCADE"))
    start_time = Column(Time)
    end_time = Column(Time)

    room = relationship("Room", back_populates="routine")
    users = relationship("User", back_populates="routine")
    # media_routine_settings = relationship("MediaRoutineSetting")
    # trv_routine_settings = relationship("TrvRoutineSetting")
    # light_routine_settings = relationship("LightRoutineSetting")

    def __init__(self, name, room_id, user_id, start_time, end_time, *args, **kwargs):
        self.name = name
        self.room_id = room_id
        self.user_id = user_id
        self.start_time = start_time
        self.end_time = end_time


class RoutineTimeEntries(Base):
    __tablename__ = "routine_time_entries"

    id = Column(Integer, primary_key=True, autoincrement=True)
    routine_id = Column(Integer, ForeignKey('routine.id'))
    timestamp = Column(TIMESTAMP)


    def __init__(self, routine_id, timestamp, *args, **kwargs):
        self.routine_id = routine_id
        self.timestamp = timestamp

