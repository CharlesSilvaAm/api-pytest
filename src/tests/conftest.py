import sys
import os

# Adiciona o diretório raiz do projeto ao sys.path
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
sys.path.insert(0, BASE_DIR)

import requests
import pytest
from src.utils.utils import load_json

@pytest.fixture(scope="session")
def base_url():
    return "https://serverest.dev"

@pytest.fixture(scope="session")
def login_payload():
    return load_json("data/login_data.json")

@pytest.fixture(scope="session")
def auth_token(login_payload):
    response = requests.post(f"{BASE_URL}/login", json=login_payload)
    assert response.status_code == 200, "Login falhou!"
    return response.json().get("authorization")

@pytest.fixture(scope="session")
def user_payload():
    return load_json("data/user_data.json")

@pytest.fixture(scope="session")
def search_payload():
    return load_json("data/search_data.json")

# def test_constants_import():
#     assert USER_KEY == "usuarios"
#     assert EMAIL_KEY == "email"