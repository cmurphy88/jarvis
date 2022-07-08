from pydantic import BaseModel, constr, StrictBool


class RoutineTimeEntries(BaseModel):
    routine_id: int
    user_id: int
    user_order: int
