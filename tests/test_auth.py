from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "Advanced Backend API is running"


def test_register_admin():
    response = client.post(
        "/api/v1/auth/register",
        json={
            "name": "Admin User",
            "email": "admin_test@gmail.com",
            "password": "admin123",
            "role": "Admin"
        }
    )

    assert response.status_code in [200, 400]