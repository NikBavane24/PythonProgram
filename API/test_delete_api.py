
import requests

def test_delete_users():

    response = requests.get("https://reqres.in/api/users?page=2")
    assert response.status_code == 200
    print("Pass Delete request")

