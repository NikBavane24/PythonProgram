

import pytest
from utils.api_helpers import get_user, create_user

@pytest.mark.api
def test_get_existing_user():
    response = get_user(2)
    assert response.status_code == 200
    assert response.json()['data']['id'] == 2

@pytest.mark.api
def test_get_non_existing_user():
    response = get_user(999)
    assert response.status_code == 404

@pytest.mark.api
def test_create_user():
    user_data = {
        "name": "morpheus",
        "job": "leader"
    }
    response = create_user(user_data)
    assert response.status_code == 201
    json_data = response.json()
    assert json_data["name"] == "morpheus"
    assert json_data["job"] == "leader"
