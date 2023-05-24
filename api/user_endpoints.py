from typing import List
import fastapi
from fastapi import Depends, HTTPException
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


router = fastapi.APIRouter()


@router.get("/user", response_model=List[User], status_code=200)
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_users(db, skip=skip, limit=limit)
    return users


@router.get("/user/{user_id}", response_model=User, status_code=200)
async def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post("/user", response_model=User, status_code=201)
async def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_username(db=db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username is already registered")
    return create_user(db=db, user=user)


@router.patch("/users/{user_id}", response_model=User, status_code=200)
async def updt_user(
    user_id: int,
    user: UserUpdate,
    db: Session = Depends(get_db),
):
    db_user = get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    else:
        return update_user(db=db, user_id=user_id, user=user)


@router.delete("/users/{user_id}", response_model=None, status_code=204)
async def exclude_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    else:
        delete_user(db=db, user_id=user_id)
