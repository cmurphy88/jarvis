from pydantic import BaseModel, constr, StrictBool


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
