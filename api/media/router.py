from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from api import db
# from api.auth.jwt import get_current_user
from . import schema
from . import services
# from api.users.schema import DisplayUser
from . import validator

router = APIRouter(tags=['Medias'], prefix='/medias')


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_media_registration(request: schema.Media, database: Session = Depends(db.get_db)):

    trv = await validator.verify_ip_address(request.ip_address, database)

    if trv:
        raise HTTPException(
            status_code=400,
            detail="This ip address is already linked to a device"
        )

    new_media = await services.new_media_register(request, database)
    return new_media


@router.get('/', response_model=List[schema.DisplayMedia])
async def get_all_medias(database: Session = Depends(db.get_db)):
    return await services.all_media(database)
