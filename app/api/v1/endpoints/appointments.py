from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.appointment import AppointmentCreate, AppointmentStatusUpdate
from app.services import appointment_service
from app.api.deps import role_required
from app.utils.response import success_response

router = APIRouter(prefix="/appointments", tags=["Appointments"])


@router.post("/")
def create_appointment(
    appointment: AppointmentCreate,
    db: Session = Depends(get_db),
    user=Depends(role_required(["Admin", "Patient"]))
):
    data = appointment_service.create_appointment(db, appointment)

    return success_response("Appointment created successfully", data)


@router.get("/")
def get_appointments(
    status: str = None,
    doctor_id: int = None,
    patient_id: int = None,
    date: str = None,
    sort_by: str = "id",
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
    user=Depends(role_required(["Admin", "Doctor", "Patient"]))
):
    data = appointment_service.get_appointments(
        db=db,
        status=status,
        doctor_id=doctor_id,
        patient_id=patient_id,
        date=date,
        sort_by=sort_by,
        skip=skip,
        limit=limit
    )

    return success_response("Appointments fetched successfully", data)


@router.put("/{appointment_id}/status")
def update_appointment_status(
    appointment_id: int,
    status_data: AppointmentStatusUpdate,
    db: Session = Depends(get_db),
    user=Depends(role_required(["Admin", "Doctor"]))
):
    data = appointment_service.update_appointment_status(
        db,
        appointment_id,
        status_data.status
    )

    return success_response("Appointment status updated successfully", data)

@router.put("/{appointment_id}/cancel")
def cancel_appointment(
    appointment_id: int,
    db: Session = Depends(get_db),
    user=Depends(role_required(["Admin", "Doctor", "Patient"]))
):
    data = appointment_service.cancel_appointment(db, appointment_id)

    return success_response("Appointment cancelled successfully", data)