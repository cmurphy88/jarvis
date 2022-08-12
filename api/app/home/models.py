from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from ..db import Base


class Home(Base):
    __tablename__ = "home"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))

    room = relationship("Room", back_populates="home")
    home_user = relationship("HomeUser", back_populates="home")

    def __init__(self, name, *args, **kwargs):
        self.name = name


class HomeUser(Base):
    __tablename__ = "home_user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    home_id = Column(Integer, ForeignKey('home.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    is_admin = Column(Boolean)

    users = relationship("User", back_populates="home_user")
    home = relationship("Home", back_populates="home_user")

    # class Config:
    #     orm_mode = True

    def __init__(self, home_id, user_id, is_admin, *args, **kwargs):
        self.home_id = home_id
        self.user_id = user_id
        self.is_admin = is_admin


