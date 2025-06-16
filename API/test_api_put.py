import requests



def test_update_user():
    payload = {
    "name": "morpheus",
    "job": "zion resident"
    }
    headers = {
        "x-api-key": "reqres-free-v1"
    }

    response = requests.put(f"https://reqres.in/api/users/2", json=payload, headers=headers)
    data = response.json()
    assert response.status_code==200
    assert data["job"]=="zion resident"
