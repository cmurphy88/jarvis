from typing import List
from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session

from api import db
from api.auth.jwt import get_current_user
from api.users.schema import User
# from api.auth.jwt import get_current_user
from . import schema
from . import services
from api.trv.schema import TrvRoutineSetting
from api.users.schema import DisplayUser

router = APIRouter(tags=['Routines'], prefix='/routines')


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_routine(request: schema.Routine, database: Session = Depends(db.get_db),
                         current_user: User = Depends(get_current_user)):
    new_routine = await services.create_routine(request, database)
    return new_routine


@router.get('/', response_model=List[schema.DisplayRoutine])
async def get_all_routines(database: Session = Depends(db.get_db),
                           current_user: User = Depends(get_current_user)):
    return await services.get_all_routines(database)


@router.get('/users/{user_id}', response_model=List[schema.DisplayRoutine])
async def get_user_routine(user_id: int, database: Session = Depends(db.get_db),
                           current_user: User = Depends(get_current_user)):
    return await services.get_user_routine(user_id, database)


@router.delete('/{routine_id}', status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
async def delete_routine_by_id(routine_id: int, database: Session = Depends(db.get_db),
                               current_user: User = Depends(get_current_user)):
    return await services.delete_routine_by_id(routine_id, database)


@router.get('/{routine_id}', response_model=schema.ShowRoutineInfo)
async def show_routine_info(routine_id: int, database: Session = Depends(db.get_db)):
    show_routine = await services.show_routine_info(routine_id, database)
    return show_routine
