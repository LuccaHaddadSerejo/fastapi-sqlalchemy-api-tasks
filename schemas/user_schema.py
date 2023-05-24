from typing import List, Optional
from pydantic import BaseModel, Field
from .task_schemas import TaskRetrieve


class UserBase(BaseModel):
    username: str
    profile: str


class UserCreate(UserBase):
    password: str

    class Config:
        orm_mode = True


class User(UserBase):
    id: int
    tasks: List[TaskRetrieve] = Field(default_factory=list)

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class UserUpdate(BaseModel):
    username: Optional[str]
    profile: Optional[str]
    password: Optional[str]

    class Config:
        orm_mode = True
