from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from ..db import Base

from . import hashing


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(255), unique=True)
    password = Column(String(255))

    routine = relationship("Routine")
    home_user = relationship("HomeUser")
    # room_user_entry = relationship("RoomUserEntry")

    def __init__(self, first_name, last_name, email, password, *args, **kwargs):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = hashing.get_password_hash(password)

    def check_password(self, password):
        return hashing.verify_password(self.password, password)
