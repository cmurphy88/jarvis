from typing import List, Optional

from fastapi import HTTPException, status
from .models import Home, HomeUser
from ..room.models import Room
from ..users.models import User


async def new_home_register(request, database) -> Home:
    new_home = Home(name=request.name)
    database.add(new_home)
    database.commit()
    database.refresh(new_home)
    return new_home


async def all_homes(database) -> List[Home]:
    homes = database.query(Home).all()
    return homes


async def get_home_by_id(home_id, database) -> Optional[Home]:
    home_info = database.query(Home).get(home_id)
    if not home_info:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Data not found !")
    return home_info


async def delete_home_by_id(home_id, database):
    database.query(Home).filter(Home.id == home_id).delete()
    database.commit()


async def add_user_to_home(request, database) -> HomeUser:
    add_user = HomeUser(home_id=request.home_id, user_id=request.user_id, is_admin=request.is_admin)
    database.add(add_user)
    database.commit()
    database.refresh(add_user)
    return add_user


async def get_all_home_users(home_id, database) -> List[User]:
    home_users = database.query(HomeUser).filter(HomeUser.home_id == home_id).all()
    user_list = list()

    for x in home_users:
        user_list.append(x.users)
    return user_list


async def get_all_users_homes(user_id, database) -> List[Home]:
    homes = database.query(HomeUser).filter(HomeUser.user_id == user_id).all()
    home_list = list()

    for x in homes:
        home_list.append(x.home)
    return home_list


async def get_all_home_rooms(home_id, database) -> List[Room]:
    rooms = database.query(Room).filter(Room.home_id == home_id).all()
    room_list = list()

    for x in rooms:
        room_list.append(x)
    return room_list
