import os
from sqlalchemy.orm import Session
from fastapi import UploadFile, HTTPException

from app.models.patient import Patient
from app.models.file import FileMetadata
from app.utils.validators import validate_file

UPLOAD_DIR = "app/uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)


def upload_patient_file(db: Session, patient_id: int, file: UploadFile):
    patient = db.query(Patient).filter(Patient.id == patient_id).first()

    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")

    content = file.file.read()

    validate_file(file.content_type, len(content))

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as f:
        f.write(content)

    metadata = FileMetadata(
        patient_id=patient_id,
        file_name=file.filename,
        file_type=file.content_type,
        file_size=len(content)
    )

    db.add(metadata)
    db.commit()
    db.refresh(metadata)

    return metadata


def get_patient_files(db: Session, patient_id: int):
    return db.query(FileMetadata).filter(
        FileMetadata.patient_id == patient_id
    ).all()