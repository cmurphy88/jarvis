from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from api import db
from . import schema
from . import services
from . import validator

router = APIRouter(tags=['Cameras'], prefix='/cameras')


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_camera(request: schema.Camera, database: Session = Depends(db.get_db)):
    camera = await validator.verify_camera_exist(request.ip_address, database)

    if camera:
        raise HTTPException(
            status_code=400,
            detail="A camera with this ip address already exists in the system"
        )

    new_camera = await services.new_camera_register(request, database)
    return new_camera


@router.get('/', response_model=List[schema.DisplayCamera])
async def get_all_cameras(database: Session = Depends(db.get_db)):
    return await services.all_cameras(database)


@router.get('/{camera_id}', response_model=schema.DisplayCamera)
async def get_camera_by_id(camera_id: int, database: Session = Depends(db.get_db)):
    return await services.get_camera_by_id(camera_id, database)


@router.delete('/{camera_id}', status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
async def delete_camera_by_id(camera_id: int, database: Session = Depends(db.get_db)):
    return await services.delete_camera_by_id(camera_id, database)
