from typing import List, Optional

from fastapi import HTTPException, status
from . import models
# from . models import HomeUser
from api.users.models import User


async def new_media_register(request, database) -> models.Media:
    new_media = models.Media(name=request.name, ip_address=request.ip_address, is_playing=request.is_playing)
    database.add(new_media)
    database.commit()
    database.refresh(new_media)
    return new_media


async def all_media(database) -> List[models.Media]:
    medias = database.query(models.Media).all()
    return medias


async def delete_media_by_id(media_id, database):
    database.query(models.Media).filter(models.Media.id == media_id).delete()
    database.commit()
