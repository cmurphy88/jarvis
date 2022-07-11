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


async def delete_trv_by_id(trv_id, database):
    database.query(models.Trv).filter(models.Trv.id == trv_id).delete()
    database.commit()


async def add_trv_settings(request, database) -> models.TrvRoutineSetting:
    new_trv_settings = models.TrvRoutineSetting(trv_id=request.trv_id,
                                                routine_id=request.routine_id,
                                                temperature=request.temperature,
                                                is_active=request.is_active)
    database.add(new_trv_settings)
    database.commit()
    database.refresh(new_trv_settings)
    return new_trv_settings
