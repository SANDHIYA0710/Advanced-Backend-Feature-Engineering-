# 🏥 Advanced Backend & Feature Engineering - Hospital Management API

## 📌 Project Objective

This project is developed using **FastAPI** to build an advanced backend application with clean architecture, real-world business logic, JWT authentication, role-based authorization, appointment management, file handling, background tasks, and unit testing.

The backend simulates a **Hospital Management System** where:

- Users can register/login with roles
- Doctors can be managed
- Patients can be managed
- Appointments can be booked and tracked
- Password reset functionality is available
- Patient files can be uploaded securely
- APIs are protected using JWT token authentication

---

# 🚀 Tech Stack Used

- Python 3.11
- FastAPI
- Uvicorn
- SQLAlchemy ORM
- SQLite Database
- Pydantic
- JWT Authentication
- Passlib + bcrypt
- OAuth2PasswordBearer
- Pytest
- Multipart File Upload

---

# 📁 Professional Backend Folder Structure

```text
backend/
│── app/
│   │── main.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   ├── security.py
│   │   └── constants.py
│   │
│   ├── db/
│   │   ├── base.py
│   │   ├── session.py
│   │   └── init_db.py
│   │
│   ├── models/
│   │   ├── user.py
│   │   ├── doctor.py
│   │   ├── patient.py
│   │   ├── appointment.py
│   │   └── file.py
│   │
│   ├── schemas/
│   │   ├── user.py
│   │   ├── auth.py
│   │   ├── doctor.py
│   │   ├── patient.py
│   │   ├── appointment.py
│   │   └── file.py
│   │
│   ├── repositories/
│   │   ├── user_repo.py
│   │   ├── doctor_repo.py
│   │   └── appointment_repo.py
│   │
│   ├── services/
│   │   ├── auth_service.py
│   │   ├── user_service.py
│   │   ├── doctor_service.py
│   │   ├── patient_service.py
│   │   ├── appointment_service.py
│   │   └── file_service.py
│   │
│   ├── api/
│   │   ├── deps.py
│   │   └── v1/
│   │       ├── router.py
│   │       └── endpoints/
│   │           ├── auth.py
│   │           ├── users.py
│   │           ├── doctors.py
│   │           ├── patients.py
│   │           ├── appointments.py
│   │           └── files.py
│   │
│   ├── utils/
│   │   ├── response.py
│   │   ├── pagination.py
│   │   └── validators.py
│   │
│   ├── middleware/
│   │   └── error_handler.py
│   │
│   ├── background/
│   │   └── tasks.py
│   │
│   └── uploads/
│
│── tests/
│   ├── test_auth.py
│   └── test_appointments.py
│
│── .env
│── requirements.txt
└── README.md


🔐 Key Backend Features Implemented
✅ 1. Advanced JWT Authentication
User Registration
User Login
JWT Access Token Generation
Protected APIs using Bearer Token
OAuth2PasswordBearer Integration
✅ 2. Password Security
Password hashing using bcrypt
Password verification during login
Forgot Password API
Reset Password API using secure JWT reset token
✅ 3. Role Based Access Control (RBAC)

Three user roles are implemented:

Admin
Doctor
Patient

API access is restricted based on roles.

Examples:

Only Admin can create/update/delete doctors
Only Admin can view all users
Patients can create appointments
Doctors/Admin can approve or reject appointments
✅ 4. Doctor Management Module

Implemented APIs:

Create Doctor
Get All Doctors
Get Doctor By ID
Update Doctor
Delete Doctor
Search Doctor by name/specialization
Sorting & Pagination supported
✅ 5. Patient Management Module

Implemented APIs:

Create Patient
Get All Patients
Get Patient By ID
Update Patient
Delete Patient
Search Patient by name/phone
Sorting & Pagination supported
✅ 6. Enhanced Appointment Management

Implemented:

Book Appointment
Validate appointment time slot
Prevent double booking for same doctor
Filter appointments by:
status
doctor_id
patient_id
date
Pagination & Sorting
Appointment Status Flow
Pending
Approved
Rejected
Completed
Cancelled
Separate APIs Available For:
Update Appointment Status
Cancel Appointment
✅ 7. Secure File Upload Module

Patient report files can be uploaded.

Implemented validations:

File type validation
File size validation
Store uploaded file metadata in database

Allowed file types:

PDF
PNG
JPEG
✅ 8. Background Tasks

FastAPI BackgroundTasks are used for:

Sending password reset token simulation
✅ 9. Standard API Response Format

Every API returns:

{
  "success": true,
  "message": "Operation successful",
  "data": {}
}

This maintains consistent API response handling.

✅ 10. Global Exception Handling

A global error handler is implemented to catch unexpected backend exceptions and return clean JSON errors.

✅ 11. Clean Service Layer Architecture

The project follows enterprise backend design:

Models Layer
Schemas Layer
Repository Layer
Service Layer
API Layer
Middleware Layer
Utility Layer

This keeps business logic separate and maintainable.

✅ 12. Unit Testing using Pytest

Basic test cases are added for:

Authentication module
Appointment module
⚙️ Installation Steps
Clone Repository
git clone https://github.com/lokeswarreddy810/Advanced_Backend.git
cd Advanced_Backend
Install Required Packages
pip install -r requirements.txt
Run Backend Server
python -m uvicorn app.main:app --reload

Server runs on:

http://127.0.0.1:8000

Swagger Documentation:

http://127.0.0.1:8000/docs
🔑 Authentication Flow
Register User

POST:

/api/v1/auth/register

Example:

{
  "name": "loki",
  "email": "loki@gmail.com",
  "password": "123456",
  "role": "Admin"
}
Login User

POST:

/api/v1/auth/login

Use:

username = loki@gmail.com
password = 123456

This generates JWT access token.

Swagger Authorization

Click Authorize in Swagger and login using:

username
password

No client id / client secret required.

🔁 Forgot Password & Reset Password Flow
Forgot Password
POST /api/v1/auth/forgot-password

Returns secure reset token.

Reset Password
POST /api/v1/auth/reset-password

Use generated token + new password.

📅 Appointment Booking Example
{
  "doctor_id": 1,
  "patient_id": 1,
  "appointment_date": "2026-05-10T10:00:00"
}

Automatically status:

Pending

Then can be changed to:

Approved
Rejected
Completed
Cancelled
🧪 Run Unit Tests
pytest
👨‍💻 Developed For

Advanced Backend & Feature Engineering Assignment

Implemented using professional FastAPI backend standards with real-world scalable folder architecture.

✅ Final Outcome

This project successfully demonstrates:

enterprise backend architecture
JWT authentication
RBAC authorization
advanced appointment workflow
secure password management
file upload handling
testing
clean scalable code design