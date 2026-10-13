import json

from app import app


def test_login_requires_email_and_password():
    client = app.test_client()

    response = client.post("/login", json={})

    assert response.status_code == 400
    payload = response.get_json()
    assert payload["success"] is False
    assert "required" in payload["message"].lower()


def test_register_then_login_uses_saved_account(monkeypatch, tmp_path):
    store_path = tmp_path / "users.json"
    monkeypatch.setattr("app.USER_STORE_PATH", store_path)
    client = app.test_client()

    registration = client.post("/register", json={
        "full_name": "Bade Hari Preetham",
        "email": "test@mohallamart.com",
        "phone": "+919876543210",
        "password": " Test@12345 ",
    })

    assert registration.status_code == 201
    stored_user = json.loads(store_path.read_text(encoding="utf-8"))["users"][0]
    assert stored_user["full_name"] == "Bade Hari Preetham"
    assert stored_user["password_hash"] != " Test@12345 "
    assert "password" not in stored_user

    response = client.post("/login", json={
        "email": "TEST@mohallamart.com",
        "password": " Test@12345 ",
    })

    assert response.status_code == 200
    payload = response.get_json()
    assert payload["success"] is True
    assert payload["user"]["full_name"] == "Bade Hari Preetham"
    assert "password_hash" not in payload["user"]


def test_register_rejects_duplicate_email(monkeypatch, tmp_path):
    monkeypatch.setattr("app.USER_STORE_PATH", tmp_path / "users.json")
    client = app.test_client()
    details = {
        "full_name": "Test User",
        "email": "test@mohallamart.com",
        "phone": "+919876543210",
        "password": "Test@12345",
    }

    assert client.post("/register", json=details).status_code == 201
    duplicate = client.post("/register", json={**details, "email": " TEST@mohallamart.com "})
    assert duplicate.status_code == 409


def test_login_rejects_wrong_password(monkeypatch, tmp_path):
    monkeypatch.setattr("app.USER_STORE_PATH", tmp_path / "users.json")
    client = app.test_client()
    client.post("/register", json={
        "full_name": "Test User",
        "email": "test@mohallamart.com",
        "phone": "+919876543210",
        "password": "Test@12345",
    })

    response = client.post("/login", json={
        "email": "test@mohallamart.com",
        "password": "wrong-password",
    })
    assert response.status_code == 401