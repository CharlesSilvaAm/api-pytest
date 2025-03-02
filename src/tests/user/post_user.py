import sys
import os
import requests
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from src.utils.constants import USER_KEY, EMAIL_KEY

@pytest.mark.parametrize("endpoint", ["/usuarios"],)
def test_deve_realizar_cadastro_com_sucesso(endpoint, user_payload, base_url, search_payload):
    response_get = requests.get(base_url + endpoint, params=search_payload)
    data = response_get.json().get(USER_KEY, [])
    id_especifico = next((item["_id"] for item in data if item[EMAIL_KEY] == search_payload[EMAIL_KEY]), None)
    if id_especifico:
        requests.delete(f"{base_url}{endpoint}/{id_especifico}")
    response = requests.post(base_url + endpoint, json=user_payload)
    json_response = response.json()
    assert response.status_code == 201