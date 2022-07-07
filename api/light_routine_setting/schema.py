from pydantic import BaseModel, constr, StrictBool


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
