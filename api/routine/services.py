from typing import List

from . import models
from api.users.models import User


async def create_routine(request, database) -> models.Routine:
    new_routine = models.Routine(room_id=request.room_id,
                                 user_id=request.user_id,
                                 start_time=request.start_time,
                                 end_time=request.end_time
                                 )
    database.add(new_routine)
    database.commit()
    database.refresh(new_routine)
    return new_routine


async def get_all_routines(database) -> List[models.Routine]:
    routines = database.query(models.Routine).all()
    return routines


async def get_user_routine(user_id, database) -> List[models.Routine]:
    user_routines = database.query(models.Routine).filter(models.Routine.user_id == user_id).all()
    routine_list = list()
    for x in user_routines:
        routine_list.append(x)
    return routine_list


async def delete_routine_by_id(routine_id, database):
    database.query(models.Routine).filter(models.Routine.id == routine_id).delete()
    database.commit()
