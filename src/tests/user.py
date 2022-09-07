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


def test_create_user_if_he_already_exists(client: TestClient):
    response = client.post(
        url="/user/register/",
        json={
            "name": "test",
            "password": "test",
        }
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "User already exists"}


def test_auth_user(client: TestClient):
    response = client.post(
        url="/user/login/",
        json={
            "name": "test",
            "password": "test",
        }
    )
    assert response.status_code == 200
    assert response.json().keys() == {"id", "token"}


def test_auth_user_if_he_does_not_exist(client: TestClient):
    response = client.post(
        url="/user/login/",
        json={
            "name": "test1",
            "password": "test",
        }
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "User does not exist"}


def test_auth_user_if_password_is_wrong(client: TestClient):
    response = client.post(
        url="/user/login/",
        json={
            "name": "test",
            "password": "test1",
        }
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "Wrong password"}
    