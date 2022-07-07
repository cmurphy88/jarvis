from typing import List, Optional

from fastapi import HTTPException, status
from . import models
# from . models import HomeUser
from api.users.models import User


async def new_home_register(request, database) -> models.Home:
    new_home = models.Home(name=request.name)
    database.add(new_home)
    database.commit()
    database.refresh(new_home)
    return new_home


async def all_homes(database) -> List[models.Home]:
    homes = database.query(models.Home).all()
    return homes


async def get_home_by_id(home_id, database) -> Optional[models.Home]:
    home_info = database.query(models.Home).get(home_id)
    if not home_info:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Data not found !")
    return home_info


async def delete_home_by_id(home_id, database):
    database.query(models.Home).filter(models.Home.id == home_id).delete()
    database.commit()


async def add_user_to_home(request, database) -> models.HomeUser:
    add_user = models.HomeUser(home_id=request.home_id, user_id=request.user_id, is_admin=request.is_admin)
    database.add(add_user)
    database.commit()
    database.refresh(add_user)
    return add_user


async def get_all_home_users(home_id, database) -> List[User]:
    home_users = database.query(models.HomeUser).filter(models.HomeUser.home_id == home_id).all()
    user_list = list()

    for x in home_users:
        user_list.append(x.users)
    return user_list
