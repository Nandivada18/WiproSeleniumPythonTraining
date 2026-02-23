#1. Write a pytest fixture that generates an authentication token once per session and use it in multiple API test cases.
import pytest

def test_get_user(auth_token):
    print(f"Using token: {auth_token}")
    assert auth_token is not None
def test_update_user(auth_token):
    print(f"Using token: {auth_token}")
    assert auth_token.startswith("ABC")

#2. Create a fixture that creates a test user via API before a test and deletes the user after test execution using yield.
def test_user_profile(test_user):
    assert test_user["username"] == "pytest_user"


#3. Write a test that validates JSON response schema from an API endpoint.
from unittest.mock import patch
import requests
from jsonschema import validate

@patch("requests.get")
def test_user_api_schema(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "id": 1,
        "username": "testuser",
        "email": "test@test.com",
        "is_active": True
    }

    response = requests.get("https://fakeapi.com/user/1")

    user_schema = {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "username": {"type": "string"},
            "email": {"type": "string"},
            "is_active": {"type": "boolean"}
        },
        "required": ["id", "username", "email", "is_active"]
    }

    validate(response.json(), user_schema)

#4. Implement a parametrized test that validates multiple HTTP status codes (200, 400, 401, 500).
import pytest
@pytest.mark.parametrize("status_code",[200,400,401,500])
def test_httpstatuscode(status_code):
    if status_code == 200 :
        print("200 K")
        assert status_code == 200
    elif status_code == 400:
        print("bad request")
        assert status_code == 400
    elif status_code == 401:
        print("Unauthorized")
        assert status_code == 401
    else:
        print("Server unavailable")
        assert status_code == 500


#5. Create a fixture chain: base_url -> auth_token -> user -> test case. Explain execution order.
def test_user_profile(user):
    print("Running test case")
    assert user["username"] == "testuser"
    assert user["token_used"] == "ABC123"
