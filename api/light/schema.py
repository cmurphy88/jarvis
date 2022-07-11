from pydantic import BaseModel, constr, StrictBool


class Light(BaseModel):
    ip_address: constr(min_length=2, max_length=50)


class DisplayLight(BaseModel):
    id: int
    ip_address: str

    class Config:
        orm_mode = True


class LightRoom(BaseModel):
    light_id: int
    room_id: int


class LightRoutineSetting(BaseModel):
    light_id: int
    routine_id: int
    media_url: str
    is_playing: StrictBool


class DisplayLightRoutineSetting(BaseModel):
    id: int
    light_id: int
    routine_id: int
    media_url: str
    is_playing: StrictBool

    class Config:
        orm_mode = True

