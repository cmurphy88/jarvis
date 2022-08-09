from typing import List, Union

from fastapi import HTTPException, status

from . import models
from api.trv.models import TrvRoutineSetting
from .schema import RoutineInfo, LightRoutineSettingView, MediaRoutineSettingView, TrvRoutineSettingView, RoutineDevices
from ..light.models import LightRoutineSetting, Light
from ..media.models import MediaRoutineSetting
from ..users.models import User


async def create_routine(request, database) -> models.Routine:
    new_routine = models.Routine(room_id=request.room_id,
                                 user_id=request.user_id,
                                 start_time=request.start_time,
                                 end_time=request.end_time
                                 )

    light_routing_settings = []
    for x in request.devices:
        if x.type == "light":
            print("light")
        if x.type == "media":
            print("media")

    new_routine.light_routine_settings = light_routing_settings

    database.add(new_routine)
    database.commit()
    database.refresh(new_routine)
    return new_routine


def create_light_setting(light_device, database) :
    light = database.query(Light).get(light_device.id)

    if not light:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Light " + light_device.id + " does not exist!")

    # Build up light here and return
    return LightRoutineSetting()


async def get_all_routines(database) -> List[models.Routine]:
    routines = database.query(models.Routine).all()
    return routines


async def get_user_routine(user_id, database) -> List[RoutineInfo]:
    user_routines = database.query(models.Routine).filter(models.Routine.user_id == user_id).all()

    routine_list = list()
    user = database.query(User).get(user_id)

    for x in user_routines:
        username = user.first_name + ' ' + user.last_name

        lights = map_light_to_view(x.light_routine_settings)
        media = map_media_to_view(x.media_routine_settings)
        trv = map_trv_to_view(x.trv_routine_settings)

        devices = []
        devices.extend(lights)
        devices.extend(media)
        devices.extend(trv)

        routine_info = RoutineInfo(id=x.id, name=x.name, user=username, start_time=x.start_time, end_time=x.end_time,
                                   devices=devices)
        routine_list.append(routine_info)

    return routine_list


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

    user = database.query(User).get(routine.user_id)

    username = user.first_name + ' ' + user.last_name

    lights = map_light_to_view(routine.light_routine_settings)
    media = map_media_to_view(routine.media_routine_settings)
    trv = map_trv_to_view(routine.trv_routine_settings)

    devices = []
    devices.extend(lights)
    devices.extend(media)
    devices.extend(trv)

    routine_info = RoutineInfo(id=routine.id, name=routine.name, user=username,
                               start_time=routine.start_time, end_time=routine.end_time, devices=devices)

    return routine_info


def map_light_to_view(lights):
    lights_view = []
    for li in lights:
        lights_view.append(LightRoutineSettingView(id=li.id, name=li.device.name, brightness=li.brightness,
                                                   is_active=li.is_active))

    return lights_view


def map_media_to_view(medias):
    medias_view = []
    for x in medias:
        medias_view.append(MediaRoutineSettingView(id=x.id, name=x.device.name, media_url=x.media_url,
                                                   is_active=x.is_active))

    return medias_view


def map_trv_to_view(trvs):
    trv_view = []
    for x in trvs:
        trv_view.append(TrvRoutineSettingView(id=x.id, name=x.device.name, temperature=x.temperature,
                                              is_active=x.is_active))

    return trv_view
