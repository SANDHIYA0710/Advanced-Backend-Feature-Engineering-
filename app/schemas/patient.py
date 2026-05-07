from pydantic import BaseModel, Field
from typing import Optional


class PatientCreate(BaseModel):
    name: str
    age: int = Field(gt=0)
    phone: str


class PatientUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = Field(default=None, gt=0)
    phone: Optional[str] = None


class PatientResponse(BaseModel):
    id: int
    name: str
    age: int
    phone: str

    class Config:
        from_attributes = True