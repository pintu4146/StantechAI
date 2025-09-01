import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_item_endpoint():
    response = client.post("/items/", json={"title": "Integration Book", "description": "First Book"})
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Integration Book"
    assert "id" in data

def test_read_items_endpoint():
    response = client.get("/items/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert any(item["title"] == "Integration Book" for item in data)
