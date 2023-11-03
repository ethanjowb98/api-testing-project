from configurations.constants import GlobalConstants
from configurations.credentials import AdminCredentials
from configurations.constants import StatusCodes
from request_actions.auth.auth_data import AuthDataAssertions
from request_actions.auth.auth_requests import add_auth_decorator
import requests
import json
from jsonpath import jsonpath
from pytest import assume, mark

@mark.dependency()
def test_admin_auth_token_creation():
    """
    Test case to create an auth token for the admin user.

    Returns:
        str: The auth token for the admin user.
    """
    # GATHER DATA
    url = add_auth_decorator(GlobalConstants.URL)
    data = {
        "username": AdminCredentials.USERNAME,
        "password": AdminCredentials.PASSWORD
    }

    # SEND REQUEST
    auth_req = requests.post(url=url, data=data)

    # ASSERTIONS
    if assume(auth_req.status_code == StatusCodes.OK):
        json_response = json.loads(auth_req.text)
        token = jsonpath(json_response, 'token')[0]
        return token

def test_admin_auth_token_creation_with_invalid_credentials():
    """
    Test case to create an auth token for the admin user with invalid credentials.

    Returns:
        str: The auth token for the admin user.
    """
    # GATHER DATA
    url = add_auth_decorator(GlobalConstants.URL)
    data = {
        "username": AdminCredentials.INVALID_USERNAME,
        "password": AdminCredentials.INVALID_PASSWORD
    }

    # SEND REQUEST
    auth_req = requests.post(url=url, data=data)
    json_response = json.loads(auth_req.text)  # Convert JSON string to dict

    # ASSERTIONS
    assume(
        jsonpath(
            json_response,
            AuthDataAssertions.AUTH_BAD_REQUEST_KEY
        )[0] == AuthDataAssertions.AUTH_BAD_REQUEST_DATA
    )
