from datetime import time
from typing import Optional

from pydantic import BaseModel, constr

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


class ShowRoutineInfo(BaseModel):
    id: int
    room_id: int
    user_id: int
    start_time: time
    end_time: time
    trv: DisplayTrv

    class Config:
        orm_mode: True
