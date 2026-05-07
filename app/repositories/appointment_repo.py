from sqlalchemy.orm import Session

from app.models.appointment import Appointment


def get_appointment_by_id(db: Session, appointment_id: int):
    return db.query(Appointment).filter(Appointment.id == appointment_id).first()


def get_appointments(db: Session):
    return db.query(Appointment)


def create_appointment(db: Session, appointment: Appointment):
    db.add(appointment)
    db.commit()
    db.refresh(appointment)

    return appointment