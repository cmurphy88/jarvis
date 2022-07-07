from typing import List

from . import models


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
