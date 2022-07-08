from typing import List, Optional

from fastapi import HTTPException, status
from . import models
from api.routine.models import Routine


async def new_user_register(request, database) -> models.User:
    new_user = models.User(first_name=request.first_name, last_name=request.last_name, email=request.email,
                           password=request.password)
    database.add(new_user)
    database.commit()
    database.refresh(new_user)
    return new_user


async def all_users(database) -> List[models.User]:
    users = database.query(models.User).all()
    return users


async def get_user_by_id(user_id, database) -> Optional[models.User]:
    user_info = database.query(models.User).get(user_id)
    if not user_info:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Data not found !")
    return user_info


async def delete_user_by_id(user_id, database):
    database.query(models.User).filter(models.User.id == user_id).delete()
    database.commit()


async def get_all_user_routines(user_id, database) -> List[Routine]:
    routine_info = database.query(Routine).filter(Routine.user_id == user_id).all()
    routine_list = list()
    for x in routine_info:
        routine_list.append(x)
    return routine_list
