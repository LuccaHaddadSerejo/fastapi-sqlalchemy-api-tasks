from sqlalchemy.orm import Session
from database.models.user_model import User
from schemas.user_schema import UserCreate


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def create_user(db: Session, user: UserCreate):
    db_user = User(username=user.username, status=user.status, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user_id: User, user: UserCreate):
    db_user = db.query(User).filter(User.id == user_id).first()
    if user.username:
        db_user.username = user.username
    if user.password:
        db_user.password = user.password
    if user.status:
        db_user.status = user.status
    db.commit()
    return db_user


def delete_user(db: Session, user_id: User):
    db_user = db.query(User).filter(User.id == user_id).first()
    db.delete(db_user)
    db.commit()
