from typing import List, Optional
from fastapi import HTTPException, status
from . import models
from api.media.models import MediaRoom
from api.trv.models import TrvRoom
from api.light.models import LightRoom
from api.room.models import RoomUserEntry
from api.routine.models import Routine


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


async def add_media_to_room(request, database) -> MediaRoom:
    add_media = MediaRoom(media_id=request.media_id, room_id=request.room_id)
    database.add(add_media)
    database.commit()
    database.refresh(add_media)
    return add_media


async def add_trv_to_room(request, database) -> TrvRoom:
    add_trv = TrvRoom(trv_id=request.trv_id, room_id=request.room_id)
    database.add(add_trv)
    database.commit()
    database.refresh(add_trv)
    return add_trv


async def add_light_to_room(request, database) -> LightRoom:
    add_light = LightRoom(light_id=request.light_id, room_id=request.room_id)
    database.add(add_light)
    database.commit()
    database.refresh(add_light)
    return add_light


async def add_user_to_room(request, database) -> RoomUserEntry:
    add_user = RoomUserEntry(user_id=request.user_id, room_id=request.room_id)
    database.add(add_user)
    database.commit()
    database.refresh(add_user)
    return add_user


async def get_all_room_routines(room_id, database) -> List[Routine]:
    routine_info = database.query(Routine).filter(Routine.room_id == room_id).all()
    routine_list = list()
    for x in routine_info:
        routine_list.append(x)
    return routine_list

    # if not routine_info:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Data not found !")
    # return routine_info


# async def get_all_home_users(home_id, database) -> List[User]:
#     home_users = database.query(models.HomeUser).filter(models.HomeUser.home_id == home_id).all()
#     user_list = list()
#
#     for x in home_users:
#         user_list.append(x.users)
#     return user_list

# async def all_rooms(database) -> List[models.Room]:
#     rooms = database.query(models.Room).all()
#     return rooms



