from typing import List, Optional

from fastapi import HTTPException, status
from . import models
# from . models import HomeUser
from api.users.models import User


async def new_trv_register(request, database) -> models.Trv:
    new_trv = models.Trv(name=request.name, ip_address=request.ip_address)
    database.add(new_trv)
    database.commit()
    database.refresh(new_trv)
    return new_trv


async def all_trv(database) -> List[models.Trv]:
    trvs = database.query(models.Trv).all()
    return trvs
