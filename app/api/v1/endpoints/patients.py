from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.patient import PatientCreate, PatientUpdate
from app.services import patient_service
from app.api.deps import role_required
from app.utils.response import success_response

router = APIRouter(prefix="/patients", tags=["Patients"])


@router.post("/")
def create_patient(
    patient: PatientCreate,
    db: Session = Depends(get_db),
    user=Depends(role_required(["Admin", "Patient"]))
):
    data = patient_service.create_patient(db, patient)

    return success_response("Patient created successfully", data)


@router.get("/")
def get_patients(
    search: str = None,
    sort_by: str = "id",
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
    user=Depends(role_required(["Admin", "Doctor"]))
):
    data = patient_service.get_patients(
        db=db,
        search=search,
        sort_by=sort_by,
        skip=skip,
        limit=limit
    )

    return success_response("Patients fetched successfully", data)


@router.get("/{patient_id}")
def get_patient(
    patient_id: int,
    db: Session = Depends(get_db),
    user=Depends(role_required(["Admin", "Doctor", "Patient"]))
):
    data = patient_service.get_patient_by_id(db, patient_id)

    return success_response("Patient fetched successfully", data)


@router.put("/{patient_id}")
def update_patient(
    patient_id: int,
    patient: PatientUpdate,
    db: Session = Depends(get_db),
    user=Depends(role_required(["Admin", "Patient"]))
):
    data = patient_service.update_patient(db, patient_id, patient)

    return success_response("Patient updated successfully", data)


@router.delete("/{patient_id}")
def delete_patient(
    patient_id: int,
    db: Session = Depends(get_db),
    user=Depends(role_required(["Admin"]))
):
    patient_service.delete_patient(db, patient_id)

    return success_response("Patient deleted successfully")