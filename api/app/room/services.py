from typing import List, Optional
from fastapi import HTTPException, status
from . import models
from ..media.models import MediaRoom
from ..trv.models import TrvRoom
from ..light.models import LightRoom
from ..room.models import RoomUserEntry
from ..routine.models import Routine
from ..routine.schema import RoutineInfo
from ..routine.services import map_light_to_view, map_media_to_view, map_trv_to_view


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


async def get_all_room_routines(room_id, database) -> List[RoutineInfo]:
    room_routines = database.query(Routine).filter(Routine.room_id == room_id).all()

    routine_list = list()

    for x in room_routines:
        username = x.users.first_name + ' ' + x.users.last_name

        lights = map_light_to_view(x.light_routine_settings)
        media = map_media_to_view(x.media_routine_settings)
        trv = map_trv_to_view(x.trv_routine_settings)

        devices = []
        devices.extend(lights)
        devices.extend(media)
        devices.extend(trv)

        routine_info = RoutineInfo(id=x.id, name=x.name, user=username, start_time=x.start_time, end_time=x.end_time,
                                   devices=devices)
        routine_list.append(routine_info)

    return routine_list

