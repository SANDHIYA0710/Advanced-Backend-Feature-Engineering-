from fastapi import FastAPI

from app.db.init_db import init_db
from app.api.v1.router import api_router
from app.middleware.error_handler import global_exception_handler

app = FastAPI(
    title="Advanced Backend & Feature Engineering",
    description="FastAPI backend with JWT, RBAC, services, repositories, file upload and testing",
    version="1.0.0"
)


@app.on_event("startup")
def startup_event():
    init_db()


app.include_router(api_router, prefix="/api/v1")

app.add_exception_handler(Exception, global_exception_handler)


@app.get("/")
def home():
    return {
        "message": "Advanced Backend API is running"
    }