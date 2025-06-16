import requests

def test_get_users_page_2():

    response = requests.get("https://reqres.in/api/users?page=2")
    assert response.status_code == 200
    assert response.json()["page"] == 2
    assert response.json()["data"][0]["id"]==7
    assert response.json()["data"][0]["email"] == "michael.lawson@reqres.in"
    assert response.json()["data"][1]["first_name"]=="Lindsay"
