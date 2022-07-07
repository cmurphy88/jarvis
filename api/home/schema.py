from pydantic import BaseModel, constr, StrictBool


class Home(BaseModel):
    name: constr(min_length=2, max_length=50)


class DisplayHome(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class HomeUser(BaseModel):
    home_id: int
    user_id: int
    is_admin: StrictBool

    class Config:
        orm_mode = True


class DisplayHomeUser(BaseModel):
    id: int
    home_id: int
    user_id: int
    is_admin: StrictBool

    class Config:
        orm_mode: True
