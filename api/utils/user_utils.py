from sqlalchemy.orm import Session
from models.user_models import User
from schemas.user_schema import UserCreate
from fastapi import HTTPException
from .jwt_utils import get_hashed_password


def get_user(db: Session, user: User, user_id: int):
    if user.profile != "admin":
        raise HTTPException(status_code=401, detail="You dont have permission")
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


def get_users(db: Session, user: User, skip: int = 0, limit: int = 10):
    if user.profile != "admin":
        raise HTTPException(status_code=401, detail="You dont have permission")
    return db.query(User).offset(skip).limit(limit).all()


def create_user(db: Session, user: UserCreate):
    db_user = get_user_by_username(db=db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username is already registered")
    password_hash = get_hashed_password(user.password)
    db_user = User(username=user.username, profile=user.profile, password=password_hash)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user_id: int, user_data: dict, user: User):
    if user.profile != "admin":
        raise HTTPException(status_code=401, detail="You dont have permission")
    db_user = get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    for field, value in user_data.items():
        setattr(db_user, field, value)
    db.commit()
    return db_user


def delete_user(db: Session, user: User, user_id: int):
    if user.profile != "admin":
        raise HTTPException(status_code=401, detail="You dont have permission")
    db_user = get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(db_user)
    db.commit()
