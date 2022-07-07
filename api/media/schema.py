from pydantic import BaseModel, constr, StrictBool


class Media(BaseModel):
    name: constr(min_length=2, max_length=50)
    ip_address: constr(min_length=2, max_length=50)
    is_playing: StrictBool


class DisplayMedia(BaseModel):
    id: int
    name: str
    ip_address: str
    is_playing: StrictBool

    class Config:
        orm_mode = True
