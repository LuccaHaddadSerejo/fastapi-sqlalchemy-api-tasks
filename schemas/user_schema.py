from typing import Optional
from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    status: str


class UserCreate(UserBase):
    password: str

    class Config:
        orm_mode = True


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class UserUpdate(BaseModel):
    username: Optional[str]
    status: Optional[str]
    password: Optional[str]

    class Config:
        orm_mode = True
