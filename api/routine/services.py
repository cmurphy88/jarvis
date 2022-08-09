from typing import List

from fastapi import HTTPException, status

from . import models
from api.trv.models import TrvRoutineSetting
from .schema import ShowRoutineInfo, LightRoutineSettingView, MediaRoutineSettingView, TrvRoutineSettingView
from ..light.models import LightRoutineSetting
from ..media.models import MediaRoutineSetting


async def create_routine(request, database) -> models.Routine:
    new_routine = models.Routine(room_id=request.room_id,
                                 user_id=request.user_id,
                                 start_time=request.start_time,
                                 end_time=request.end_time
                                 )
    database.add(new_routine)
    database.commit()
    database.refresh(new_routine)
    return new_routine



async def get_all_routines(database) -> List[models.Routine]:
    routines = database.query(models.Routine).all()
    return routines


async def get_user_routine(user_id, database) -> List[models.Routine]:
    user_routines = database.query(models.Routine).filter(models.Routine.user_id == user_id).all()
    routine_list = list()
    for x in user_routines:
        routine_list.append(x)
    return routine_list


async def delete_routine_by_id(routine_id, database):
    database.query(models.Routine).filter(models.Routine.id == routine_id).delete()
    database.commit()


async def show_routine_info(routine_id, database) -> RoutineInfo:
    routine = database.query(models.Routine).get(routine_id)
    if not routine:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Routine does not exist!")

    routine_info.id = routine.room_id
    routine_info.room_id = routine.room_id
    routine_info.name = routine.name
    routine_info.user_id = routine.user_id
    routine_info.start_time = routine.start_time
    routine_info.end_time = routine.end_time

    routine_info.light = map_light_to_view(light_info)
    routine_info.media = map_media_to_view(media_info)
    routine_info.trv = map_trv_to_view(trv_info)

    return routine_info


def map_light_to_view(lights):
    lights_view = []
    for x in lights:
        light = LightRoutineSettingView()
        light.id = lights.id
        light.name = lights.name
        light.brightness = lights.brightness
        light.is_active = lights.is_active
        lights_view.append(light)

        print(lights_view[0].name)

    return lights_view


def map_media_to_view(medias):
    medias_view = []
    for x in medias:
        media = MediaRoutineSettingView()
        media.id = medias.id
        media.name = medias.name
        media.media_url = medias.media_url
        media.is_active = medias.is_active
        medias_view.append(media)

        print(medias_view[0].name)

    return medias_view


def map_trv_to_view(trvs):
    trv_view = []
    for x in trvs:
        trv = TrvRoutineSettingView()
        trv.id = trvs.id
        trv.name = trvs.name
        trv.media_url = trvs.media_url
        trv.is_active = trvs.is_active
        trv_view.append(trv)

        print(trv_view[0].name)

    return trv_view
