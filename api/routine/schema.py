from datetime import time
from typing import Optional, List

from pydantic import BaseModel, constr, StrictBool

from api.light.schema import DisplayLight
from api.media.schema import DisplayMedia
from api.trv.schema import DisplayTrv, Trv


class TrvSettings(BaseModel):
    id: int
    temperature: int


class LightSettings(BaseModel):
    id: int
    brightness: int


class MediaSettings(BaseModel):
    id: int
    media_url: str


class Routine(BaseModel):
    room_id: int
    user_id: int
    start_time: time
    end_time: time
    trv: Optional[TrvSettings]
    light: Optional[LightSettings]
    media: Optional[MediaSettings]


class DisplayRoutine(BaseModel):
    id: int
    room_id: int
    user_id: int
    start_time: time
    end_time: time

    class Config:
        orm_mode = True


class RoutineTimeEntries(BaseModel):
    id: int
    user_id: int
    user_order: int


class TrvRoutineSetting(BaseModel):
    id: int
    name: str
    temperature: int
    is_active: StrictBool
    type: str = "trv"

    class Config:
        orm_mode = True


class LightRoutineSetting(BaseModel):
    id: int
    name: str
    brightness: int
    is_active: StrictBool
    type: str = "light"

    class Config:
        orm_mode = True


class MediaRoutineSetting(BaseModel):
    id: int
    name: str
    media_url: str
    is_active: StrictBool
    type: str = "media"

    class Config:
        orm_mode = True


class ShowRoutineInfo(BaseModel):
    id: int
    room_id: int
    user_id: int
    start_time: time
    end_time: time
    trv: List[TrvRoutineSetting]
    light: List[LightRoutineSetting]
    media: List[MediaRoutineSetting]

    class Config:
        orm_mode: True
