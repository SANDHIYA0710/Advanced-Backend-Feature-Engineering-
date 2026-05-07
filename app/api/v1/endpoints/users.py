from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.services import user_service
from app.api.deps import role_required
from app.utils.response import success_response

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/")
def get_users(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
    user=Depends(role_required(["Admin"]))
):
    data = user_service.get_users(db, skip, limit)

    return success_response("Users fetched successfully", data)