from pydantic import BaseModel
from datetime import datetime


class FileResponse(BaseModel):
    id: int
    patient_id: int
    file_name: str
    file_type: str
    file_size: int
    uploaded_at: datetime

    class Config:
        from_attributes = True