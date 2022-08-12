from typing import List, Optional

from . import models


async def new_light_register(request, database) -> models.Light:
    new_light = models.Light(ip_address=request.ip_address)
    database.add(new_light)
    database.commit()
    database.refresh(new_light)
    return new_light


async def all_light(database) -> List[models.Light]:
    lights = database.query(models.Light).all()
    return lights


async def delete_light_by_id(light_id, database):
    database.query(models.Light).filter(models.Light.id == light_id).delete()
    database.commit()

