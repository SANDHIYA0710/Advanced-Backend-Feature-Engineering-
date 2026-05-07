from fastapi import HTTPException

from app.core.constants import ALLOWED_FILE_TYPES, MAX_FILE_SIZE


def validate_file(file_type: str, file_size: int):
    if file_type not in ALLOWED_FILE_TYPES:
        raise HTTPException(
            status_code=400,
            detail="Invalid file type"
        )

    if file_size > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=400,
            detail="File size must be below 2MB"
        )