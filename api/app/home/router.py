from typing import List

from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from . import schema
from . import services
from . import validator
from .schema import DisplayHome
from .. import db
from ..room.schema import DisplayRoom
from ..users.schema import DisplayUser

router = APIRouter(tags=['Homes'], prefix='/homes')


@router.post('', status_code=status.HTTP_201_CREATED)
async def create_home(request: schema.Home, database: Session = Depends(db.get_db)):
    user = await validator.verify_home_exist(request.name, database)

    if user:
        raise HTTPException(
            status_code=400,
            detail="A home with this name already exists in the system"
        )

    new_home = await services.new_home_register(request, database)
    return new_home


@router.get('', response_model=List[schema.DisplayHome])
async def get_all_homes(database: Session = Depends(db.get_db)):
    return await services.all_homes(database)


@router.get('/{home_id}', response_model=schema.DisplayHome)
async def get_home_by_id(home_id: int, database: Session = Depends(db.get_db)):
    return await services.get_home_by_id(home_id, database)


@router.get('/{name}', response_model=schema.DisplayHome)
async def get_home_by_name(name: str, database: Session = Depends(db.get_db)):
    return await services.get_home_by_name(name, database)


@router.post('/create', status_code=status.HTTP_201_CREATED)
async def create_home_and_add_user(request: schema.CreateHomeAndAddUser, database: Session = Depends(db.get_db)):
    return await services.create_home_and_add_user(request, database)


@router.delete('/{home_id}', status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
async def delete_home_by_id(home_id: int, database: Session = Depends(db.get_db)):
    return await services.delete_home_by_id(home_id, database)


@router.post('/{home_id}/users', status_code=status.HTTP_201_CREATED)
async def add_user_to_home(request: schema.HomeUser, database: Session = Depends(db.get_db)):
    add_user = await services.add_user_to_home(request, database)
    return add_user


@router.get('/{home_id}/users', response_model=List[DisplayUser])
async def get_user_home(home_id: int, database: Session = Depends(db.get_db)):
    return await services.get_all_home_users(home_id, database)


@router.get('/users/{user_id}', response_model=List[DisplayHome])
async def get_all_users_homes(user_id: int, database: Session = Depends(db.get_db)):
    return await services.get_all_users_homes(user_id, database)


@router.get('/{home_id}/rooms', response_model=List[DisplayRoom])
async def get_all_home_rooms(home_id: int, database: Session = Depends(db.get_db)):
    return await services.get_all_home_rooms(home_id, database)
