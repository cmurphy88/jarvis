from pydantic import BaseModel, constr, StrictBool


class MediaRoutineSetting(BaseModel):
    media_id: int
    routine_id: int
    media_url: str
    is_playing: StrictBool


class DisplayMediaRoutineSetting(BaseModel):
    id: int
    media_id: int
    routine_id: int
    media_url: str
    is_playing: StrictBool

    class Config:
        orm_mode = True
