from configurations.constants import StatusCodes
from configurations.constants import GlobalConstants
from request_actions.booking.booking_requests import add_booking_decorator
from .test_get_booking import test_get_booking_id_details
from .test_create_auth_token import test_admin_auth_token_creation
from .test_update_booking import test_update_created_booking, test_partial_update_created_booking
from pytest import assume
import requests

def test_delete_created_booking():
    """
    Test case to delete a booking.
    """
    # GATHER DATA
    url = add_booking_decorator(GlobalConstants.URL)
    booking_id = test_get_booking_id_details()
    headers = {
        "Content-Type": "application/json",
        "Cookie": f"token={test_admin_auth_token_creation()}"
    }

    # SEND REQUEST
    booking_req = requests.delete(url=f"{url}/{booking_id}", headers=headers)

    # ASSERTIONS
    assume(booking_req.status_code == StatusCodes.CREATED)
    deleted_booking_req = requests.delete(url=f"{url}/{booking_id}", headers=headers)
    assume(deleted_booking_req.status_code == StatusCodes.METHOD_NOT_ALLOWED)

def test_delete_updated_booking():
    """
    Test case to delete a booking.
    """
    # GATHER DATA
    url = add_booking_decorator(GlobalConstants.URL)
    booking_id = test_update_created_booking()
    headers = {
        "Content-Type": "application/json",
        "Cookie": f"token={test_admin_auth_token_creation()}"
    }

    # SEND REQUEST
    booking_req = requests.delete(url=f"{url}/{booking_id}", headers=headers)

    # ASSERTIONS
    assume(booking_req.status_code == StatusCodes.CREATED)
    deleted_booking_req = requests.delete(url=f"{url}/{booking_id}", headers=headers)
    assume(deleted_booking_req.status_code == StatusCodes.METHOD_NOT_ALLOWED)

def test_delete_partial_updated_booking():
    """
    Test case to delete a booking.
    """
    # GATHER DATA
    url = add_booking_decorator(GlobalConstants.URL)
    booking_id = test_partial_update_created_booking()
    headers = {
        "Content-Type": "application/json",
        "Cookie": f"token={test_admin_auth_token_creation()}"
    }

    # SEND REQUEST
    booking_req = requests.delete(url=f"{url}/{booking_id}", headers=headers)

    # ASSERTIONS
    assume(booking_req.status_code == StatusCodes.CREATED)
    deleted_booking_req = requests.delete(url=f"{url}/{booking_id}", headers=headers)
    assume(deleted_booking_req.status_code == StatusCodes.METHOD_NOT_ALLOWED)
