import requests


def test_create_user():
    payload = {
        "name": "John",
        "job": "Engineer"
    }
    headers = {
        "x-api-key": "reqres-free-v1"
    }

    response = requests.post(f"https://reqres.in/api/users", json=payload, headers=headers)

    assert response.status_code == 201, f"Expected 201, got {response.status_code}"

    data = response.json()
    assert data["name"] == "John"
    assert data["job"] == "Engineer"
    assert "id" in data
    assert "createdAt" in data
