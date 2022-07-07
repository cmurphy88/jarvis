from sqlalchemy import Time

from pydantic import BaseModel, constr


class Routine(BaseModel):
    room_id: int
    user_id: int
    start_time: str
    end_time: str


class DisplayRoutine(BaseModel):
    id: int
    room_id: int
    user_id: int
    start_time: str
    end_time: str
