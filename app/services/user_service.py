from sqlalchemy.orm import Session

from app.repositories import user_repo


def get_users(db: Session, skip: int = 0, limit: int = 10):
    return user_repo.get_users(db, skip, limit)