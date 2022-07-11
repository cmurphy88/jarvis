from pydantic import BaseModel, constr, StrictBool


class Trv(BaseModel):
    name: constr(min_length=2, max_length=50)
    ip_address: constr(min_length=2, max_length=50)


class DisplayTrv(BaseModel):
    id: int
    name: str
    ip_address: str

    class Config:
        orm_mode = True


class TrvRoom(BaseModel):
    trv_id: int
    room_id: int


class TrvRoutineSetting(BaseModel):
    trv_id: int
    routine_id: int
    media_url: str
    is_playing: StrictBool


class DisplayTrvRoutineSetting(BaseModel):
    id: int
    trv_id: int
    routine_id: int
    media_url: str
    is_playing: StrictBool

    class Config:
        orm_mode = True
