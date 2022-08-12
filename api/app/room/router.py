from typing import List
from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session
from .. import db
from . import schema
from . import services
from ..media.schema import MediaRoom
from ..trv.schema import TrvRoom
from ..light.schema import LightRoom
from ..room.schema import RoomUserEntry
from ..routine.schema import RoutineInfo

router = APIRouter(tags=['Rooms'], prefix='/rooms')


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_room_registration(request: schema.Room, database: Session = Depends(db.get_db)):
    new_room = await services.new_room_register(request, database)
    return new_room


@router.get('/', response_model=List[schema.DisplayRoom])
async def get_all_rooms(database: Session = Depends(db.get_db)):
    return await services.all_rooms(database)


@router.get('/{room_id}', response_model=schema.DisplayRoom)
async def get_room_by_id(room_id: int, database: Session = Depends(db.get_db)):
    return await services.get_room_by_id(room_id, database)


# @router.post('/{room_id/users', status_code=status.HTTP_201_CREATED)
# async def add_user_to_room(request: schema.DisplayRoom, database: Session = Depends(db.get_db)):
#     return await services.add_user_to_room(request.room_id, database)


@router.delete('/{room_id}', status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
async def delete_room_by_id(room_id: int, database: Session = Depends(db.get_db)):
    return await services.delete_room_by_id(room_id, database)


@router.post('/{room_id}/medias', status_code=status.HTTP_201_CREATED)
async def add_media_to_room(request: MediaRoom, database: Session = Depends(db.get_db)):
    return await services.add_media_to_room(request, database)


@router.post('/{room_id}/trvs', status_code=status.HTTP_201_CREATED)
async def add_trv_to_room(request: TrvRoom, database: Session = Depends(db.get_db)):
    return await services.add_trv_to_room(request, database)


@router.post('/{room_id}/lights', status_code=status.HTTP_201_CREATED)
async def add_light_to_room(request: LightRoom, database: Session = Depends(db.get_db)):
    return await services.add_light_to_room(request, database)


@router.post('/{room_id}/users', status_code=status.HTTP_201_CREATED)
async def add_user_to_room(request: RoomUserEntry, database: Session = Depends(db.get_db)):
    return await services.add_user_to_room(request, database)


@router.get('/{room_id}/routines', response_model=List[RoutineInfo])
async def get_room_routines(room_id: int, database: Session = Depends(db.get_db)):
    return await services.get_all_room_routines(room_id, database)
