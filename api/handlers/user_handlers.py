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
async def read_users_endpoint(
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
    skip: int = 0,
    limit: int = 10,
):
    users = get_users(db, user=user, skip=skip, limit=limit)
    return users


@router.get("/users/{user_id}", response_model=User, status_code=200)
async def read_user_endpoint(
    user_id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)
):
    db_user = get_user(user_id=user_id, db=db, user=user)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post("/users", response_model=User, status_code=201)
async def create_user_endpoint(
    user_data: UserCreate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    return create_user(user_data=user_data, db=db, user=user)


@router.patch("/users/{user_id}", response_model=User, status_code=200)
async def update_user_endpoint(
    user_id: int,
    user_data: UserUpdate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    update_data = user_data.dict(exclude_unset=True)
    return update_user(user_id=user_id, user_data=update_data, db=db, user=user)


@router.delete("/users/{user_id}", response_model=None, status_code=204)
async def delete_user_endpoint(
    user_id: int,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    delete_user(user_id=user_id, db=db, user=user)
