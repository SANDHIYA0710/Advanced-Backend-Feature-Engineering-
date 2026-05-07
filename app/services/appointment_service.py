from fastapi import HTTPException
from sqlalchemy.orm import Session
from datetime import datetime

from app.models.doctor import Doctor
from app.models.patient import Patient
from app.models.appointment import Appointment
from app.schemas.appointment import AppointmentCreate
from app.repositories import appointment_repo

allowed_status = ["Pending", "Approved", "Rejected", "Completed", "Cancelled"]


def validate_time_slot(appointment_date: datetime):
    if appointment_date <= datetime.utcnow():
        raise HTTPException(
            status_code=400,
            detail="Appointment time must be in the future"
        )

    if appointment_date.minute not in [0, 30]:
        raise HTTPException(
            status_code=400,
            detail="Appointment must be booked on 30-minute slots"
        )


def create_appointment(db: Session, appointment: AppointmentCreate):
    validate_time_slot(appointment.appointment_date)

    doctor = db.query(Doctor).filter(Doctor.id == appointment.doctor_id).first()

    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")

    if not doctor.is_active:
        raise HTTPException(status_code=400, detail="Doctor is inactive")

    patient = db.query(Patient).filter(Patient.id == appointment.patient_id).first()

    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")

    existing = db.query(Appointment).filter(
        Appointment.doctor_id == appointment.doctor_id,
        Appointment.appointment_date == appointment.appointment_date,
        Appointment.status.in_(["Pending", "Approved"])
    ).first()

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Doctor already booked for this time slot"
        )

    new_appointment = Appointment(
        doctor_id=appointment.doctor_id,
        patient_id=appointment.patient_id,
        appointment_date=appointment.appointment_date,
        status="Pending"
    )

    return appointment_repo.create_appointment(db, new_appointment)


def get_appointments(
    db: Session,
    status: str = None,
    doctor_id: int = None,
    patient_id: int = None,
    date: str = None,
    sort_by: str = "id",
    skip: int = 0,
    limit: int = 10
):
    query = appointment_repo.get_appointments(db)

    if status:
        query = query.filter(Appointment.status == status)

    if doctor_id:
        query = query.filter(Appointment.doctor_id == doctor_id)

    if patient_id:
        query = query.filter(Appointment.patient_id == patient_id)

    if date:
        query = query.filter(Appointment.appointment_date.contains(date))

    if sort_by == "date":
        query = query.order_by(Appointment.appointment_date)
    elif sort_by == "status":
        query = query.order_by(Appointment.status)
    else:
        query = query.order_by(Appointment.id)

    return query.offset(skip).limit(limit).all()


def update_appointment_status(db: Session, appointment_id: int, status: str):
    allowed_status = ["Pending", "Approved", "Rejected", "Completed"]

    if status not in allowed_status:
        raise HTTPException(status_code=400, detail="Invalid appointment status")

    appointment = appointment_repo.get_appointment_by_id(db, appointment_id)

    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")

    appointment.status = status

    db.commit()
    db.refresh(appointment)

    return appointment

def cancel_appointment(db: Session, appointment_id: int):
    appointment = appointment_repo.get_appointment_by_id(db, appointment_id)

    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")

    if appointment.status == "Completed":
        raise HTTPException(
            status_code=400,
            detail="Completed appointment cannot be cancelled"
        )

    appointment.status = "Cancelled"

    db.commit()
    db.refresh(appointment)

    return appointment