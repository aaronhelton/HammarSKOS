import json
from fastapi.testclient import TestClient
from api.main import app
from api.models import Vocabulary

client = TestClient(app)

def test_get_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"hello": "world"}

def test_get_vocabularies():
    response = client.get("/vocabularies")
    assert response.status_code == 200
    assert len(response.json()) == 1