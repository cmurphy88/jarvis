from datetime import datetime
from typing import List, Union

from fastapi import HTTPException, status
from pyasn1.compat.octets import null

from . import models
from ..auth.jwt import get_current_user
from ..trv.models import TrvRoutineSetting
from .schema import RoutineInfo, LightRoutineSettingView, MediaRoutineSettingView, TrvRoutineSettingView, \
    RoutineDevices, CreateRoutineResponse, CreateRoutineTimeEntry
from ..light.models import LightRoutineSetting, Light
from ..media.models import MediaRoutineSetting
from ..media.models import Media
from ..users.models import User
from ..trv.models import Trv


def build_light_routine_settings(database, request):
    light_list = []
    for d in request.devices:
        if d.type == 'light':
            light = database.query(Light).filter(Light.name == d.name).first()
            if not light:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Light " +
                                                                                    d.name + " does not exist!")
            light_routine = LightRoutineSetting(light_id=light.id, brightness=d.brightness,
                                                is_active=d.is_active)

            light_list.append(light_routine)

    return light_list


def build_media_routine_settings(database, request):
    media_list = []
    for d in request.devices:
        if d.type == 'media':
            media = database.query(Media).filter(Media.name == d.name).first()
            if not media:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Media " +
                                                                                    d.name + " does not exist!")
            media_routine = MediaRoutineSetting(media_id=media.id, media_url=d.media_url,
                                                is_active=d.is_active)

            media_list.append(media_routine)

    return media_list


async def create_routine(request, database) -> CreateRoutineResponse:
    new_routine = models.Routine(name=request.name,
                                 room_id=request.room_id,
                                 user_id=request.user_id,
                                 start_time=request.start_time,
                                 end_time=request.end_time,
                                 )

    light_devices = build_light_routine_settings(database, request)
    media_devices = build_media_routine_settings(database, request)
    new_routine.light_routine_settings = light_devices
    new_routine.media_routine_settings = media_devices

    database.add(new_routine)
    database.commit()
    database.refresh(new_routine)

    return CreateRoutineResponse(routine_id=new_routine.id)


def create_light_setting(light_device, database) :
    light = database.query(Light).get(light_device.id)

    if not light:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Light " +
                                                                            light_device.id + " does not exist!")

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

        lights = map_light_to_view(x.light_routine_settings, database)
        media = map_media_to_view(x.media_routine_settings, database)
        trv = map_trv_to_view(x.trv_routine_settings, database)

        devices = []
        devices.extend(lights)
        devices.extend(media)
        devices.extend(trv)

        routine_info = RoutineInfo(id=x.id, room_id=x.room_id, name=x.name, user=username, start_time=x.start_time,
                                   end_time=x.end_time,
                                   devices=devices)
        routine_list.append(routine_info)

    return routine_list


async def get_active_routine(room_id, database) -> RoutineInfo:
    user_routines = database.query(models.Routine).filter(models.Routine.room_id == room_id).all()

    routine_list = list()

    # user_email = await get_current_user().email

    current_time = datetime.now().time()

    for x in user_routines:
        user_id = x.user_id
        user = database.query(User).get(user_id)
        username = user.first_name + ' ' + user.last_name

        lights = map_light_to_view(x.light_routine_settings, database)
        media = map_media_to_view(x.media_routine_settings, database)
        trv = map_trv_to_view(x.trv_routine_settings, database)

        devices = []
        devices.extend(lights)
        devices.extend(media)
        devices.extend(trv)

        routine_info = RoutineInfo(id=x.id, user_id=x.user_id, room_id=x.room_id, name=x.name, user=username,
                                   start_time=x.start_time,
                                   end_time=x.end_time,
                                   devices=devices)
        routine_list.append(routine_info)

    current_list = []

    for x in routine_list:
        if x.start_time < current_time:
            if x.end_time > current_time:
                current_list.append(x)

    if len(current_list) == 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No active routine!")

    return current_list[0]


async def get_active_routine_by_room(room_id, user_id, database) -> List[RoutineInfo]:
    user_routines = database.query(models.Routine).filter(models.Routine.room_id == room_id).all()

    routine_list = list()
    current_time = datetime.now().time()

    for x in user_routines:
        user_id = x.user_id
        user = database.query(User).get(user_id)
        username = user.first_name + ' ' + user.last_name

        lights = map_light_to_view(x.light_routine_settings, database)
        media = map_media_to_view(x.media_routine_settings, database)
        trv = map_trv_to_view(x.trv_routine_settings, database)

        devices = []
        devices.extend(lights)
        devices.extend(media)
        devices.extend(trv)

        routine_info = RoutineInfo(id=x.id, room_id=x.room_id, user_id=user_id, name=x.name, user=username,
                                   start_time=x.start_time,
                                   end_time=x.end_time,
                                   devices=devices)
        routine_list.append(routine_info)

    current_list = []

    for x in routine_list:
        if (x.user_id == user_id) and (x.start_time < current_time) and (x.end_time > current_time):
            current_list.append(x)

    if len(current_list) == 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No active routine!")

    if len(current_list) > 0:
        is_active = await is_routine_active(current_list[0], database)
        if not is_active:
            await create_time_entries(current_list[0], database)
        else:
            raise HTTPException(status_code=status.HTTP_200_OK, detail="Routine already active!")

    return current_list


async def is_routine_active(routine, database):
    current_date = datetime.now().date()

    entries = database.query(models.RoutineTimeEntries).filter(models.RoutineTimeEntries.routine_id == routine.id)
    for x in entries:
        if x.time_entry.date() == current_date:
            return True
        else:
            continue


async def create_time_entries(routine, database):
    current_time_date = datetime.now()
    new_time_entry = models.RoutineTimeEntries(routine_id=routine.id, time_entry=current_time_date)

    database.add(new_time_entry)
    database.commit()
    database.refresh(new_time_entry)


async def create_routine_time_entry(request, database) -> CreateRoutineTimeEntry:

    # select routine time entries by routine id, check if time exists in table, if yes, exit, return response code 200
    # if entry doesn't exist, return the routine info

    new_routine_time_entry = models.RoutineTimeEntries(routine_id=request.routine_id,
                                                       time_entry=request.time_entry)

    database.add(new_routine_time_entry)
    database.commit()
    database.refresh(new_routine_time_entry)

    return new_routine_time_entry


async def delete_routine_by_id(routine_id, database):
    database.query(models.Routine).filter(models.Routine.id == routine_id).delete()
    database.commit()


async def show_routine_info(routine_id, database) -> RoutineInfo:
    routine = database.query(models.Routine).get(routine_id)
    if not routine:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Routine does not exist!")

    user = database.query(User).get(routine.user_id)
    username = user.first_name + ' ' + user.last_name
    lights = map_light_to_view(routine.light_routine_settings, database)
    media = map_media_to_view(routine.media_routine_settings, database)
    trv = map_trv_to_view(routine.trv_routine_settings, database)

    devices = []
    devices.extend(lights)
    devices.extend(media)
    devices.extend(trv)

    routine_info = RoutineInfo(id=routine.id, name=routine.name, user=username,
                               start_time=routine.start_time, end_time=routine.end_time, devices=devices)

    return routine_info


def map_light_to_view(lights, database):
    lights_view = []
    for li in lights:
        name = get_light_names(li, database)
        lights_view.append(LightRoutineSettingView(id=li.id, name=name, brightness=li.brightness,
                                                   is_active=li.is_active))

    return lights_view


def get_light_names(li, database):
    light = database.query(Light).filter(Light.id == li.id).first()
    return light.name


def map_media_to_view(medias, database):
    medias_view = []
    for x in medias:
        media_name = get_media_names(x, database)
        medias_view.append(MediaRoutineSettingView(id=x.id, name=media_name, media_url=x.media_url,
                                                   is_active=x.is_active))

    return medias_view


def get_media_names(med, database):
    media = database.query(Media).filter(Media.id == med.id).first()
    return media.name


def map_trv_to_view(trvs, database):
    trv_view = []
    for x in trvs:
        trv_name = get_trv_names(x, database)
        trv_view.append(TrvRoutineSettingView(id=x.id, name=trv_name, temperature=x.temperature,
                                              is_active=x.is_active))

    return trv_view


def get_trv_names(trv, database):
    trv = database.query(Trv).filter(Trv.id == trv.id).first()
    return trv.name


def get_all_routine_time_entries(database) -> List[models.RoutineTimeEntries]:
    entries = database.query(models.RoutineTimeEntries).all()
    return entries
