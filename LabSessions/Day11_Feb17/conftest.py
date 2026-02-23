import pytest
import requests
#1
@pytest.fixture(scope="session")
def auth_token():
    print("Generating token for the session")
    token = "ABC123"
    yield token
    print("Session Ended")

#5
@pytest.fixture(scope="session")
def base_url():
    print("Providing base URL")
    return "https://api.example.com"
#User fixture (depends on base_url and auth_token)
@pytest.fixture(scope="function")
def user(base_url, auth_token):
    print("Creating user with token:", auth_token)
    user_data = {
        "username": "testuser",
        "token_used": auth_token,
        "base_url_used": base_url
    }
    return user_data

#2
@pytest.fixture(scope="function")
def test_user(base_url, auth_token):

    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }

    # Setup - Create user
    print("Creating test user...")
    response = requests.post(
        f"{base_url}/users",
        json={
            "username": "pytest_user",
            "email": "pytest_user@test.com",
            "password": "Password123"
        },
        headers=headers
    )

    assert response.status_code == 201
    user_data = response.json()
    user_id = user_data["id"]
    yield user_data

    # Teardown - Delete user
    print("Deleting test user...")
    delete_response = requests.delete(
        f"{base_url}/users/{user_id}",
        headers=headers
    )

    assert delete_response.status_code in [200, 204]
