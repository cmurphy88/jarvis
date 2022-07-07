from typing import List

from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from api import db
from . import schema
from . import services
from . import validator
from api.users.schema import DisplayUser

router = APIRouter(tags=['Lights'], prefix='/lights')


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_light_registration(request: schema.Light, database: Session = Depends(db.get_db)):

    trv = await validator.verify_ip_address(request.ip_address, database)

    if trv:
        raise HTTPException(
            status_code=400,
            detail="This ip address is already linked to a device"
        )

    new_light = await services.new_light_register(request, database)
    return new_light


@router.get('/', response_model=List[schema.DisplayLight])
async def get_all_lights(database: Session = Depends(db.get_db)):
    return await services.all_light(database)
