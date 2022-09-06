from fastapi.testclient import TestClient


def test_create_user(client: TestClient):
    response = client.post(
        url="/user/register/",
        json={
            "name": "test",
            "password": "test",
        }
    )
    assert response.status_code == 200
    assert response.json().keys() == {"id", "token"}