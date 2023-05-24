from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.db_setup import get_db
from schemas.user_schema import UserCreate, User, UserUpdate
from api.utils.user_utils import (
    get_user,
    get_users,
    create_user,
    delete_user,
    update_user,
)
from api.deps.user_deps import get_current_user


router = APIRouter()


@router.get("/users", response_model=List[User], status_code=200)
async def read_users(
    user: User = Depends(get_current_user),
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
):
    users = get_users(db, skip=skip, limit=limit, user=user)
    return users


@router.get("/users/{user_id}", response_model=User, status_code=200)
async def read_user(
    user_id: int, user: User = Depends(get_current_user), db: Session = Depends(get_db)
):
    db_user = get_user(db=db, user_id=user_id, user=user)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post("/users", response_model=User, status_code=201)
async def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db=db, user=user)


@router.patch("/users/{user_id}", response_model=User, status_code=200)
async def update_user_endpoint(
    user_id: int,
    user_data: UserUpdate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    update_data = user_data.dict(exclude_unset=True)
    return update_user(db=db, user_id=user_id, user_data=update_data, user=user)


@router.delete("/users/{user_id}", response_model=None, status_code=204)
async def delete_user_endpoint(
    user_id: int,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    delete_user(db=db, user_id=user_id, user=user)
