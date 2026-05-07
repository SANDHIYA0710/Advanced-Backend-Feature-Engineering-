from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.patient import Patient
from app.schemas.patient import PatientCreate, PatientUpdate


def create_patient(db: Session, patient: PatientCreate):
    new_patient = Patient(
        name=patient.name,
        age=patient.age,
        phone=patient.phone
    )

    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)

    return new_patient


def get_patients(
    db: Session,
    search: str = None,
    sort_by: str = "id",
    skip: int = 0,
    limit: int = 10
):
    query = db.query(Patient)

    if search:
        query = query.filter(
            Patient.name.contains(search) |
            Patient.phone.contains(search)
        )

    if sort_by == "name":
        query = query.order_by(Patient.name)
    elif sort_by == "age":
        query = query.order_by(Patient.age)
    else:
        query = query.order_by(Patient.id)

    return query.offset(skip).limit(limit).all()


def get_patient_by_id(db: Session, patient_id: int):
    patient = db.query(Patient).filter(Patient.id == patient_id).first()

    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")

    return patient


def update_patient(db: Session, patient_id: int, data: PatientUpdate):
    patient = get_patient_by_id(db, patient_id)

    if data.name is not None:
        patient.name = data.name

    if data.age is not None:
        patient.age = data.age

    if data.phone is not None:
        patient.phone = data.phone

    db.commit()
    db.refresh(patient)

    return patient


def delete_patient(db: Session, patient_id: int):
    patient = get_patient_by_id(db, patient_id)

    db.delete(patient)
    db.commit()

    return patient