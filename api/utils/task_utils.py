from fastapi import HTTPException
from sqlalchemy.orm import Session
from database.models.user_model import Task as TaskModel
from schemas.task_schema import TaskCreate, TaskUpdate
from database.models.user_model import User
import ipdb


def get_task_by_id(db: Session, task_id: int):
    return db.query(TaskModel).filter(TaskModel.id == task_id).first()


def get_tasks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(TaskModel).offset(skip).limit(limit).all()


def get_todo_tasks(db: Session):
    return db.query(TaskModel).filter(TaskModel.status == "todo").all()


def create_task(db: Session, task: TaskCreate):
    if task.user_id is not None:
        user = db.query(User).filter(User.id == task.user_id).first()
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
    db_task = TaskModel(
        title=task.title,
        status=task.status,
        description=task.description,
        user_id=task.user_id,
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def update_task(db: Session, task_id: int, task_data: dict):
    db_task = get_task_by_id(db=db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    for field, value in task_data.items():
        setattr(db_task, field, value)
    db.commit()
    return db_task


def delete_task(db: Session, task_id: int):
    db_task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(db_task)
    db.commit()
