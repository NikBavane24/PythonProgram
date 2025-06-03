
import requests

response = requests.get("https://reqres.in/api/users?page=2")
assert response.status_code == 200

json_data = response.json()

# Validate top-level fields
assert json_data["page"] == 2
assert json_data["per_page"] == 6
assert json_data["total"] == 12
assert json_data["total_pages"] == 2

# Validate data length
assert len(json_data["data"]) == 6

assert json_data["data"][1]["email"] == "lindsay.ferguson@reqres.in"

# Validate each user object
for user in json_data["data"]:
    assert "id" in user
    assert "email" in user
    assert "first_name" in user
    assert "last_name" in user
    assert "avatar" in user
    assert user["email"].endswith("@reqres.in")
