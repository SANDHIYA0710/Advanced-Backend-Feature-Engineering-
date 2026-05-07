from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.doctor import Doctor
from app.schemas.doctor import DoctorCreate, DoctorUpdate
from app.repositories import doctor_repo


def create_doctor(db: Session, doctor: DoctorCreate):
    existing = doctor_repo.get_doctor_by_email(db, doctor.email)

    if existing:
        raise HTTPException(status_code=400, detail="Doctor email already exists")

    new_doctor = Doctor(
        name=doctor.name,
        specialization=doctor.specialization,
        email=doctor.email
    )

    return doctor_repo.create_doctor(db, new_doctor)


def get_doctors(
    db: Session,
    search: str = None,
    sort_by: str = "id",
    skip: int = 0,
    limit: int = 10
):
    query = doctor_repo.get_doctors(db)

    if search:
        query = query.filter(
            Doctor.name.contains(search) |
            Doctor.specialization.contains(search)
        )

    if sort_by == "name":
        query = query.order_by(Doctor.name)
    elif sort_by == "specialization":
        query = query.order_by(Doctor.specialization)
    else:
        query = query.order_by(Doctor.id)

    return query.offset(skip).limit(limit).all()


def get_doctor_by_id(db: Session, doctor_id: int):
    doctor = doctor_repo.get_doctor_by_id(db, doctor_id)

    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")

    return doctor


def update_doctor(db: Session, doctor_id: int, data: DoctorUpdate):
    doctor = get_doctor_by_id(db, doctor_id)

    if data.name is not None:
        doctor.name = data.name

    if data.specialization is not None:
        doctor.specialization = data.specialization

    if data.email is not None:
        doctor.email = data.email

    if data.is_active is not None:
        doctor.is_active = data.is_active

    db.commit()
    db.refresh(doctor)

    return doctor


def delete_doctor(db: Session, doctor_id: int):
    doctor = get_doctor_by_id(db, doctor_id)

    doctor_repo.delete_doctor(db, doctor)

    return doctor