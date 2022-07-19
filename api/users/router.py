from typing import List

from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from api import db
# from api.auth.jwt import get_current_user
from . import schema
from . import services
from . import validator
from api.routine.schema import DisplayRoutine
from api.auth.jwt import get_current_user


router = APIRouter(tags=['Users'], prefix='/users')


@router.get('/', response_model=List[schema.DisplayUser])
async def get_all_user(database: Session = Depends(db.get_db),
                       current_user: schema.User = Depends(get_current_user)):
    return await services.all_users(database)


@router.get('/me', response_model=schema.DisplayUser)
async def get_auth_user(database: Session = Depends(db.get_db),
                        current_user: schema.User = Depends(get_current_user)):
    return await services.get_user_by_email(current_user.email, database)


@router.get('/{user_id}', response_model=schema.DisplayUser)
async def get_user_by_id(user_id: int, database: Session = Depends(db.get_db)):
    return await services.get_user_by_id(user_id, database)


@router.delete('/{user_id}', status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
async def delete_user_by_id(user_id: int, database: Session = Depends(db.get_db),
                            current_user: schema.User = Depends(get_current_user)):
    return await services.delete_user_by_id(user_id, database)


@router.get('/{user_id}/routines', response_model=List[DisplayRoutine])
async def get_user_routines(user_id: int, database: Session = Depends(db.get_db),
                            current_user: schema.User = Depends(get_current_user)):
    return await services.get_all_user_routines(user_id, database)
