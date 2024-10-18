# backend/app/schemas/module.py

from pydantic import BaseModel
from typing import Optional

class ModuleBase(BaseModel):
    course_id: int
    title: str
    content: Optional[str] = None

class ModuleCreate(ModuleBase):
    pass

class ModuleRead(ModuleBase):
    id: int

    class Config:
        orm_mode = True
