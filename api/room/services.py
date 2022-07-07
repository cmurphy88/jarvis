from typing import List, Optional
from fastapi import HTTPException, status
from . import models


async def new_room_register(request, database) -> models.Room:
    new_room = models.Room(name=request.name, home_id=request.home_id)
    database.add(new_room)
    database.commit()
    database.refresh(new_room)
    return new_room


async def all_rooms(database) -> List[models.Room]:
    rooms = database.query(models.Room).all()
    return rooms


async def get_room_by_id(room_id, database) -> Optional[models.Room]:
    room_info = database.query(models.Room).get(room_id)
    if not room_info:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Data not found !")
    return room_info


async def delete_room_by_id(room_id, database):
    database.query(models.Room).filter(models.Room.id == room_id).delete()
    database.commit()


# def add_user_to_room(room_id, database):
#     add_user = models.Room()
#     return None
