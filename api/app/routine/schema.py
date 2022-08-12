from datetime import time
from typing import Optional, List, Union

from pydantic import BaseModel, StrictBool


class TrvSettings(BaseModel):
    id: int
    name: str
    temperature: int
    is_active: StrictBool
    type: str = "trv"


class LightSettings(BaseModel):
    id: int
    name: str
    brightness: int
    is_active: StrictBool
    type: str = "light"


class MediaSettings(BaseModel):
    id: int
    name: str
    media_url: str
    is_active: StrictBool
    type: str = "media"


class Routine(BaseModel):
    room_id: int
    user_id: int
    start_time: time
    end_time: time
    devices: List[Union[LightSettings, MediaSettings, TrvSettings]]


class DisplayRoutine(BaseModel):
    id: int
    room_id: int
    name: str
    user_id: int
    start_time: time
    end_time: time

    class Config:
        orm_mode = True


class RoutineTimeEntries(BaseModel):
    id: int
    user_id: int
    user_order: int


class LightRoutineSetting(BaseModel):
    id: int
    light_id: int
    routine_id: int
    brightness: int
    is_playing: StrictBool

    class Config:
        orm_mode = True


class TrvRoutineSetting(BaseModel):
    id: int
    light_id: int
    routine_id: int
    temperature: int
    is_playing: StrictBool

    class Config:
        orm_mode = True


class MediaRoutineSetting(BaseModel):
    id: int
    light_id: int
    routine_id: int
    media_url: str
    is_playing: StrictBool

    class Config:
        orm_mode = True


class DeviceRoutineSettingView(BaseModel):
    id: int
    name: str
    is_active: bool
    type: str


class TrvRoutineSettingView(DeviceRoutineSettingView):
    temperature: int
    type = "trv"


class LightRoutineSettingView(DeviceRoutineSettingView):
    brightness: int
    type = "light"


class MediaRoutineSettingView(DeviceRoutineSettingView):
    media_url: str
    type = "media"


class RoutineDevices(BaseModel):
    devices: List[Union[LightRoutineSettingView, MediaRoutineSettingView, TrvRoutineSettingView]]


class DeviceRoutineSettingCreate(BaseModel):
    id: int
    name: str
    is_active: bool
    type: str


class TrvRoutineSettingCreate(DeviceRoutineSettingCreate):
    temperature: int
    type = "trv"


class LightRoutineSettingCreate(DeviceRoutineSettingCreate):
    brightness: int
    type = "light"


class MediaRoutineSettingCreate(DeviceRoutineSettingCreate):
    media_url: str
    type = "media"


class RoutineDevicesCreate(BaseModel):
    devices: List[Union[TrvRoutineSettingCreate, LightRoutineSettingCreate, MediaRoutineSettingCreate]]


class RoutineInfo(BaseModel):
    id: int
    name: str
    user: str
    start_time: time
    end_time: time
    devices: List[Union[LightRoutineSettingView, MediaRoutineSettingView, TrvRoutineSettingView]]


class CreateRoutine(BaseModel):
    name: str
    room_id: int
    user_id: int
    start_time: time
    end_time: time
    light_id: Optional[int]
    room_id: Optional[int]
    devices: List[Union[LightRoutineSettingCreate, MediaRoutineSettingCreate, TrvRoutineSettingCreate]]


class CreateRoutineResponse(BaseModel):
    routine_id: int

