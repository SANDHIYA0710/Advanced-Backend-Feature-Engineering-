from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate
from app.schemas.auth import LoginSchema
from app.core.security import decode_token, hash_password
from app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
    create_reset_token
)
from app.repositories import user_repo


def register_user(db: Session, user: UserCreate):
    allowed_roles = ["Admin", "Doctor", "Patient"]

    if user.role not in allowed_roles:
        raise HTTPException(status_code=400, detail="Invalid role")

    existing_user = user_repo.get_user_by_email(db, user.email)

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = User(
        name=user.name,
        email=user.email,
        password=hash_password(user.password),
        role=user.role
    )

    return user_repo.create_user(db, new_user)


def login_user(db: Session, email: str, password: str):
    user = user_repo.get_user_by_email(db, email)

    if not user:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    if not verify_password(password, user.password):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    token = create_access_token({
        "sub": user.email,
        "role": user.role,
        "user_id": user.id
    })

    return token


def forgot_password(db: Session, email: str):
    user = user_repo.get_user_by_email(db, email)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return create_reset_token(email)

def reset_password(db: Session, token: str, new_password: str):
    payload = decode_token(token)

    email = payload.get("sub")

    user = user_repo.get_user_by_email(db, email)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.password = hash_password(new_password)

    db.commit()
    db.refresh(user)

    return user