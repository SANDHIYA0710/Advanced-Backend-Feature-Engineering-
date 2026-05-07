from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.doctor import DoctorCreate, DoctorUpdate
from app.services import doctor_service
from app.api.deps import role_required
from app.utils.response import success_response

router = APIRouter(prefix="/doctors", tags=["Doctors"])


@router.post("/")
def create_doctor(
    doctor: DoctorCreate,
    db: Session = Depends(get_db),
    user=Depends(role_required(["Admin"]))
):
    data = doctor_service.create_doctor(db, doctor)

    return success_response("Doctor created successfully", data)


@router.get("/")
def get_doctors(
    search: str = None,
    sort_by: str = "id",
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
    user=Depends(role_required(["Admin", "Doctor", "Patient"]))
):
    data = doctor_service.get_doctors(
        db=db,
        search=search,
        sort_by=sort_by,
        skip=skip,
        limit=limit
    )

    return success_response("Doctors fetched successfully", data)


@router.get("/{doctor_id}")
def get_doctor(
    doctor_id: int,
    db: Session = Depends(get_db),
    user=Depends(role_required(["Admin", "Doctor", "Patient"]))
):
    data = doctor_service.get_doctor_by_id(db, doctor_id)

    return success_response("Doctor fetched successfully", data)


@router.put("/{doctor_id}")
def update_doctor(
    doctor_id: int,
    doctor: DoctorUpdate,
    db: Session = Depends(get_db),
    user=Depends(role_required(["Admin"]))
):
    data = doctor_service.update_doctor(db, doctor_id, doctor)

    return success_response("Doctor updated successfully", data)


@router.delete("/{doctor_id}")
def delete_doctor(
    doctor_id: int,
    db: Session = Depends(get_db),
    user=Depends(role_required(["Admin"]))
):
    doctor_service.delete_doctor(db, doctor_id)

    return success_response("Doctor deleted successfully")