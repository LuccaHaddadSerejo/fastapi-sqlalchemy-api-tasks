from typing import Optional
from pydantic import BaseModel


class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: str
    user_id: Optional[int] = None


class TaskCreate(TaskBase):
    ...


class Task(TaskBase):
    id: int

    class Config:
        orm_mode = True


class TaskUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    status: Optional[str]
    user_id: Optional[int]

    class Config:
        orm_mode = True


class TaskRetrieve(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    status: str

    class Config:
        orm_mode = True
