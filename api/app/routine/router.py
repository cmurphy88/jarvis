from typing import List
from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session
import datetime

from .. import db
from ..auth.jwt import get_current_user
from ..users.schema import User
# from ..auth.jwt import get_current_user
from . import schema
from . import services

router = APIRouter(tags=['Routines'], prefix='/routines')


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_routine(request: schema.CreateRoutine, database: Session = Depends(db.get_db)):
    new_routine = await services.create_routine(request, database)
    return new_routine


@router.get('/', response_model=List[schema.DisplayRoutine])
async def get_all_routines(database: Session = Depends(db.get_db),
                           current_user: User = Depends(get_current_user)):
    return await services.get_all_routines(database)


@router.get('/users/{user_id}', response_model=List[schema.RoutineInfo])
async def get_user_routine(user_id: int, database: Session = Depends(db.get_db)):
    return await services.get_user_routine(user_id, database)


@router.get('/rooms/{room_id}/active', response_model=schema.RoutineInfo)
async def get_active_routine(room_id: int, database: Session = Depends(db.get_db)):
    return await services.get_active_routine(room_id, database)


@router.get('/rooms/{room_id}/users/{user_id}', response_model=List[schema.RoutineInfo])
async def get_active_routine_by_room(room_id: int, user_id: int, database: Session = Depends(db.get_db)):
    return await services.get_active_routine_by_room(room_id, user_id, database)


@router.delete('/{routine_id}', status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
async def delete_routine_by_id(routine_id: int, database: Session = Depends(db.get_db),
                               current_user: User = Depends(get_current_user)):
    return await services.delete_routine_by_id(routine_id, database)


@router.get('/{routine_id}', response_model=schema.RoutineInfo)
async def show_routine_info(routine_id: int, database: Session = Depends(db.get_db)):
    show_routine = await services.show_routine_info(routine_id, database)
    return show_routine


@router.post('/entries', response_model=schema.RoutineTimeEntries)
async def create_routine_time_entry(request: schema.RoutineTimeEntries, database: Session = Depends(db.get_db)):
    return await services.create_routine_time_entry(request, database)


@router.get('/entries_all', response_model=List[schema.RoutineTimeEntries])
async def get_all_routine_time_entries(database: Session = Depends(db.get_db)):
    return await services.get_all_routine_time_entries(database)
