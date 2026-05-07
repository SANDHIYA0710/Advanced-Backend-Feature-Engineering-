from fastapi import APIRouter, Depends, BackgroundTasks
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.user import UserCreate
from app.schemas.auth import ForgotPasswordSchema, ResetPasswordSchema
import app.services.auth_service as auth_service
from app.background.tasks import send_password_reset_email
from app.utils.response import success_response

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    data = auth_service.register_user(db, user)

    return success_response("User registered successfully", {
        "id": data.id,
        "name": data.name,
        "email": data.email,
        "role": data.role
    })


@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    token = auth_service.login_user(
        db=db,
        email=form_data.username,
        password=form_data.password
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }


@router.post("/forgot-password")
def forgot_password(
    data: ForgotPasswordSchema,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db)
):
    token = auth_service.forgot_password(db, data.email)

    background_tasks.add_task(send_password_reset_email, data.email, token)

    return success_response("Password reset token generated", {
        "reset_token": token
    })


@router.post("/reset-password")
def reset_password(
    data: ResetPasswordSchema,
    db: Session = Depends(get_db)
):
    auth_service.reset_password(
        db=db,
        token=data.token,
        new_password=data.new_password
    )

    return success_response("Password reset successfully")