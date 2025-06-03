import requests

BASE_URL = "https://reqres.in/api"

def get_user(user_id):
    return requests.get(f"{BASE_URL}/users/{user_id}")

def create_user(data):
    return requests.post(f"{BASE_URL}/users", json=data)
