from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends, HTTPException, status
from .utils.jwt_utils import verify_password, create_access_token, create_refresh_token
from sqlalchemy.orm import Session
from database.db_setup import get_db
from schemas.token_schema import Token
from database.models.user_model import User
import ipdb

router = APIRouter()


@router.post(
    "/login",
    summary="Create access and refresh tokens for user",
    response_model=Token,
)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    user = db.query(User).filter_by(username=form_data.username).first()

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect username or password",
        )

    hashed_pass = user.password

    if not verify_password(form_data.password, hashed_pass):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect username or password",
        )

    return {
        "access_token": create_access_token(user.id),
        "refresh_token": create_refresh_token(user.id),
    }
