import requests
import pytest


@pytest.mark.parametrize("endpoint", ["/login"])
def test_deve_realizar_login_com_sucesso(endpoint, login_payload, base_url):
    response = requests.post(base_url + endpoint, json=login_payload)
    json_response = response.json()
    assert response.status_code == 200
    assert "authorization" in json_response, TOKEN_NOT_FOUND
    assert "message" in json_response, LOGIN_SUCCESS
    assert response.headers.get("Content-Type") == "application/json; charset=utf-8"


    

