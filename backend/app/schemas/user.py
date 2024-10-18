# backend/app/schemas/user.py

from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    telegram_id: str
    username: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    language: Optional[str] = 'ru'

class UserCreate(UserBase):
    pass

class UserRead(UserBase):
    id: int
    tokens: int

    class Config:
        orm_mode = True
