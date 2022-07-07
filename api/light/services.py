from typing import List, Optional

from fastapi import HTTPException, status
from . import models
# from . models import HomeUser
from api.users.models import User


async def new_light_register(request, database) -> models.Light:
    new_light = models.Light(ip_address=request.ip_address)
    database.add(new_light)
    database.commit()
    database.refresh(new_light)
    return new_light


async def all_light(database) -> List[models.Light]:
    lights = database.query(models.Light).all()
    return lights

