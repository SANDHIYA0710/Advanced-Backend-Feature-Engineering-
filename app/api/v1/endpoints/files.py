from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.services import file_service
from app.api.deps import role_required
from app.utils.response import success_response

router = APIRouter(prefix="/files", tags=["Files"])


@router.post("/upload/{patient_id}")
def upload_file(
    patient_id: int,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    user=Depends(role_required(["Admin", "Doctor", "Patient"]))
):
    data = file_service.upload_patient_file(db, patient_id, file)

    return success_response("File uploaded successfully", data)


@router.get("/patient/{patient_id}")
def get_patient_files(
    patient_id: int,
    db: Session = Depends(get_db),
    user=Depends(role_required(["Admin", "Doctor", "Patient"]))
):
    data = file_service.get_patient_files(db, patient_id)

    return success_response("Patient files fetched successfully", data)