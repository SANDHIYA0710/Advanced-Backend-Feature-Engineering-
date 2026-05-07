# Hospital Management Backend API

## Overview

This project is a backend-driven Hospital Management System developed using FastAPI with a modular and scalable architecture. The application focuses on authentication, role-based authorization, appointment scheduling, doctor and patient management, secure file uploads, and structured API development practices.

The system is designed to simulate a real-world healthcare backend environment with clean code organization, layered architecture, and secure API handling.

---

## Core Functionalities

### Authentication & Authorization

* User Registration
* Secure Login System
* JWT Token Authentication
* OAuth2 Password Flow
* Role-Based Access Control

### Doctor Management

* Add Doctor
* View Doctors
* Update Doctor Information
* Delete Doctor
* Search & Filter Doctors

### Patient Management

* Add Patients
* Manage Patient Records
* Search Patients
* Update/Delete Patient Information

### Appointment Management

* Schedule Appointments
* Update Appointment Status
* Prevent Duplicate Time Slot Booking
* Appointment Filtering and Pagination

### File Upload System

* Upload Patient Reports
* File Validation
* Metadata Storage
* Secure File Handling

### Password Management

* Forgot Password API
* Reset Password Functionality
* Password Hashing using bcrypt

### Testing & Error Handling

* Unit Testing using Pytest
* Global Exception Handling
* Structured API Responses

---

## Technologies Used

* Python 3.14
* FastAPI
* Uvicorn
* SQLAlchemy
* SQLite
* Pydantic
* JWT Authentication
* Passlib (bcrypt)
* OAuth2PasswordBearer
* Pytest

---

## Project Structure

```text
Advanced_Backend/
│
├── app/
│   │── __init__.py
│   │── main.py
│   │
│   ├── api/
│   │   ├── __init__.py
│   │   ├── deps.py
│   │   │
│   │   └── v1/
│   │       ├── __init__.py
│   │       ├── router.py
│   │       │
│   │       └── endpoints/
│   │           ├── __init__.py
│   │           ├── auth.py
│   │           ├── doctors.py
│   │           ├── patients.py
│   │           ├── appointments.py
│   │           ├── users.py
│   │           └── files.py
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── security.py
│   │   └── constants.py
│   │
│   ├── db/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── session.py
│   │   └── init_db.py
│   │
│   ├── middleware/
│   │   ├── __init__.py
│   │   └── error_handler.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── doctor.py
│   │   ├── patient.py
│   │   ├── appointment.py
│   │   └── file.py
│   │
│   ├── repositories/
│   │   ├── __init__.py
│   │   ├── user_repo.py
│   │   ├── doctor_repo.py
│   │   ├── patient_repo.py
│   │   ├── appointment_repo.py
│   │   └── file_repo.py
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── user.py
│   │   ├── doctor.py
│   │   ├── patient.py
│   │   ├── appointment.py
│   │   └── file.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── auth_service.py
│   │   ├── user_service.py
│   │   ├── doctor_service.py
│   │   ├── patient_service.py
│   │   ├── appointment_service.py
│   │   └── file_service.py
│   │
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── validators.py
│   │   ├── pagination.py
│   │   └── response.py
│   │
│   ├── background/
│   │   ├── __init__.py
│   │   └── tasks.py
│   │
│   └── uploads/
│
├── tests/
│   ├── __init__.py
│   ├── test_auth.py
│   ├── test_doctors.py
│   ├── test_patients.py
│   └── test_appointments.py
│
├── .env
├── requirements.txt
├── README.md
└── advanced_backend.db
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/Advanced-Backend-Feature-Engineering-.git
```

### Move to Project Directory

```bash
cd Advanced-Backend-Feature-Engineering-
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Start Backend Server

```bash
python -m uvicorn app.main:app --reload
```

---

## API Documentation

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

## User Registration Example

```json
{
  "name": "Sandhiya",
  "email": "sandhiya@gmail.com",
  "password": "sandhiya123",
  "role": "Admin"
}
```

---

## Login Example

```text
username: sandhiya@gmail.com
password: sandhiya123
```

---

## Appointment Example

```json
{
  "doctor_id": 1,
  "patient_id": 1,
  "appointment_date": "2026-05-10T10:30:00"
}
```

---

## Appointment Status Values

* Pending
* Confirmed
* Completed
* Cancelled

---

## Running Test Cases

```bash
pytest
```

---

## Backend Design Highlights

* Layered Architecture
* Service & Repository Pattern
* Reusable API Design
* Modular Folder Structure
* JWT Secured Endpoints
* Scalable Backend Workflow
* Enterprise-Oriented Code Organization

---

## Conclusion

This project demonstrates backend engineering concepts including API security, authentication workflows, database integration, appointment lifecycle management, and scalable FastAPI development practices suitable for modern healthcare applications.
