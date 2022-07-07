from pydantic import BaseModel, constr, StrictBool


class Light(BaseModel):
    ip_address: constr(min_length=2, max_length=50)


class DisplayLight(BaseModel):
    id: int
    ip_address: str

    class Config:
        orm_mode = True
