from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey, Boolean, TIMESTAMP
from sqlalchemy.orm import relationship

from api.db import Base


class RoutineTimeEntries(Base):
    __tablename__ = "routine_time_entries"

    id = Column(Integer, primary_key=True, autoincrement=True)
    routine_id = Column(Integer, ForeignKey('routine.id'))
    timestamp = Column(TIMESTAMP)

    rooms = relationship("Room")
    users = relationship("User")

    def __init__(self, routine_id, timestamp, *args, **kwargs):
        self.routine_id = routine_id
        self.timestamp = timestamp
