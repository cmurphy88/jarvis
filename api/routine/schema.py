from datetime import time

from pydantic import BaseModel, constr


class Routine(BaseModel):
    room_id: int
    user_id: int
    start_time: time
    end_time: time


class DisplayRoutine(BaseModel):
    id: int
    room_id: int
    user_id: int
    start_time: time
    end_time: time

    class Config:
        orm_mode = True
