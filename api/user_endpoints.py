from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.db_setup import get_db
from schemas.user_schema import UserCreate, User, UserUpdate
from api.utils.user_utils import (
    get_user,
    get_user_by_username,
    get_users,
    create_user,
    delete_user,
    update_user,
)

router = APIRouter()


@router.get("/users", response_model=List[User], status_code=200)
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_users(db, skip=skip, limit=limit)
    return users


@router.get("/users/{user_id}", response_model=User, status_code=200)
async def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post("/users", response_model=User, status_code=201)
async def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_username(db=db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username is already registered")
    return create_user(db=db, user=user)


@router.patch("/users/{user_id}", response_model=User, status_code=200)
async def update_user_endpoint(
    user_id: int,
    user_data: UserUpdate,
    db: Session = Depends(get_db),
):
    update_data = user_data.dict(exclude_unset=True)
    return update_user(db=db, user_id=user_id, user_data=update_data)


@router.delete("/users/{user_id}", response_model=None, status_code=204)
async def delete_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    delete_user(db=db, user_id=user_id)
