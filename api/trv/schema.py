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
