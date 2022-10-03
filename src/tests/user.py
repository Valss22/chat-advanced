from httpx import AsyncClient

async def test_create_user(client: AsyncClient):
    response = await client.post(
        url="/user/register/",
        json={
            "name": "test",
            "password": "test",
        }
    )
    assert response.status_code == 200
    assert response.json().keys() == {"id", "token"}


async def test_create_user_if_he_already_exists(client: AsyncClient):
    response = await client.post(
        url="/user/register/",
        json={
            "name": "test",
            "password": "test",
        }
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "User already exists"}


async def test_auth_user(client: AsyncClient):
    response = await client.post(
        url="/user/login/",
        json={
            "name": "test",
            "password": "test",
        }
    )
    assert response.status_code == 200
    assert response.json().keys() == {"id", "token"}


async def test_auth_user_if_he_does_not_exist(client: AsyncClient):
    response = await client.post(
        url="/user/login/",
        json={
            "name": "test1",
            "password": "test",
        }
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "User does not exist"}


async def test_auth_user_if_password_is_wrong(client: AsyncClient):
    response = await client.post(
        url="/user/login/",
        json={
            "name": "test",
            "password": "test1",
        }
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "Wrong password"}
    

async def test_get_user(client: AsyncClient):
    response = await client.get(
        url="/user/",
        params={
            "name": "test",
        }
    )
    assert response.status_code == 200
    assert response.json().keys() == {"id", "name"}


async def test_get_user_if_he_does_not_exist(client: AsyncClient):
    response = await client.get(
        url="/user/",
        params={
            "name": "test1",
        }
    )
    assert response.status_code == 400
    assert response.json() == {'detail': 'User does not exist'}