from fastapi.testclient import TestClient
from src.main import app
client = TestClient(app)


def test_add():
    response = client.get("/add?a=5&b=3")
    assert response.status_code == 200
    assert response.json() == {"result": 8}


def test_subtract():
    response = client.get("/subtract?a=10&b=4")
    assert response.status_code == 200
    assert response.json() == {"result": 6}


def test_multiply():
    response = client.get("/multiply?a=6&b=7")
    assert response.status_code == 200
    assert response.json() == {"result": 42}


def test_divide():
    response = client.get("/divide?a=20&b=5")
    assert response.status_code == 200
    assert response.json() == {"result": 4}


def test_divide_by_zero():
    response = client.get("/divide?a=10&b=0")
    assert response.status_code == 400
    assert response.json() == {"detail": "Cannot divide by zero"}


def test_sqrt():
    response = client.get("/sqrt?x=16")
    assert response.status_code == 200
    assert response.json() == {"result": 4}


def test_sqrt_negative():
    response = client.get("/sqrt?x=-9")
    assert response.status_code == 400
    assert response.json() == {"detail": "Cannot take sqrt of negative number"}

