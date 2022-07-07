from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from api import db
# from api.auth.jwt import get_current_user
from . import schema
from . import services

router = APIRouter(tags=['Routine'], prefix='/routines')


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_routine(request: schema.Routine, database: Session = Depends(db.get_db)):
    new_routine = await services.create_routine(request, database)
    return new_routine


@router.get('/', response_model=List[schema.DisplayRoutine])
async def get_all_routines(database: Session = Depends(db.get_db)):
    return await services.get_all_routines(database)

