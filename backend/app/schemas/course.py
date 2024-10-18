# backend/app/schemas/course.py

from pydantic import BaseModel
from typing import Optional, List

class CourseBase(BaseModel):
    name: str
    description: Optional[str] = None

class CourseCreate(CourseBase):
    pass

class CourseRead(CourseBase):
    id: int
    modules: List['ModuleRead'] = []

    class Config:
        orm_mode = True
