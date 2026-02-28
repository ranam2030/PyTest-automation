import requests
from utils.config import API_BASE_URL

def test_get_users():
    response = requests.get(f"{API_BASE_URL}/users?page=2")
    assert response.status_code == 200
    assert "data" in response.json()