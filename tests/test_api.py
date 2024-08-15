from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_status():
    response = client.get("/status")
    assert response.status_code == 200
    assert response.json() == {"status": "API is running"}

def test_predict():
    response = client.post("/predict", json={"date": "2013-01-01", "store": 1, "item": 1})
    assert response.status_code == 200
    assert "sales" in response.json()
