from typing import List, Optional
from fastapi import HTTPException, status
from . import models


async def new_camera_register(request, database) -> models.Camera:
    new_camera = models.Camera(ip_address=request.ip_address)
    database.add(new_camera)
    database.commit()
    database.refresh(new_camera)
    return new_camera


async def all_cameras(database) -> List[models.Camera]:
    cameras = database.query(models.Camera).all()
    return cameras


async def get_camera_by_id(camera_id, database) -> Optional[models.Camera]:
    camera_info = database.query(models.Camera).get(camera_id)
    if not camera_info:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Data not found !")
    return camera_info


async def delete_camera_by_id(camera_id, database):
    database.query(models.Camera).filter(models.Camera.id == camera_id).delete()
    database.commit()
