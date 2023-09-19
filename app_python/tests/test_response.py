
from main import app


def test_response():
    with app.test_client() as test_client:
        response = test_client.get("/")
        assert response.status_code == 200
        assert b"time" in response.data

def test_error():
    with app.test_client() as test_client:
        response = test_client.get("/error")
        assert response.status_code == 404

def test_time():
    with app.test_client() as test_client:
        response = test_client.get("/")
        assert b"time" in response.data