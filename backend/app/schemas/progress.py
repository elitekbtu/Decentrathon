# backend/app/schemas/progress.py

from pydantic import BaseModel
from typing import Optional

class ProgressBase(BaseModel):
    user_id: int
    course_id: int
    module_id: int
    completed: bool = False

class ProgressCreate(ProgressBase):
    pass

class ProgressRead(ProgressBase):
    id: int

    class Config:
        orm_mode = True
