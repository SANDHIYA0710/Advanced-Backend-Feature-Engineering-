from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_appointments_without_token():
    response = client.get("/api/v1/appointments/")

    assert response.status_code == 401