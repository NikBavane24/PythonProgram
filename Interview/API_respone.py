import requests

response =requests.get("https://reqres.in/api/users/2")
assert response.status_code==200


json_data = response.json()
assert json_data["data"]["id"]==2
assert json_data["data"]["email"] == "janet.weaver@reqres.in"
assert json_data["support"]["text"] == "Tired of writing endless social media content? Let Content Caddy generate it for you."