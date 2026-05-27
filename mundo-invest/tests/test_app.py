from http import HTTPStatus

from fastapi.testclient import TestClient

from src.mundo_invest.app import app

client = TestClient(app)


def test_read_root_should_return_welcome_message(client):
    response = client.get("/")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Olá mundo"}
