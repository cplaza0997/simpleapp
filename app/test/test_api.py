from fastapi.testclient import TestClient
from ..api import router
import json
client = TestClient(router)

def test_sum_numbers():
    response = client.post("/arit", json={"o":"+","a": 1, "b": 2})
    assert response.status_code == 200
    assert response.json() == {"result": 3}
    
def test_sum_numbers_negative():
    response = client.post("/arit", json={"o":"+","a": -1, "b": -2})
    assert response.status_code == 200
    assert response.json() == {"result": -3}

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}