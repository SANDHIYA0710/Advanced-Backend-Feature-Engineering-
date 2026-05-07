from app.db.base import Base
from app.db.session import engine

from app.models.user import User
from app.models.doctor import Doctor
from app.models.patient import Patient
from app.models.appointment import Appointment
from app.models.file import FileMetadata


def init_db():
    Base.metadata.create_all(bind=engine)