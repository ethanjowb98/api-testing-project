from configurations.constants import StatusCodes
from configurations.constants import GlobalConstants
from .test_create_booking import test_create_bookings
from .test_create_auth_token import test_admin_auth_token_creation
from request_actions.booking.booking_requests import add_booking_decorator
from request_actions.booking.booking_data import BookingData, UpdateBookingData
import requests
from pytest import assume, mark
import json

@mark.dependency(depends=["test_create_bookings"])
def test_update_created_booking():
    """
    Test case to update a booking.
    """
    # GATHER DATA
    url = add_booking_decorator(GlobalConstants.URL)
    booking_id = test_create_bookings()
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Cookie": f"token={test_admin_auth_token_creation()}"
    }
    data = {
        "firstname": UpdateBookingData.FIRSTNAME,
        "lastname": UpdateBookingData.LASTNAME,
        "totalprice": UpdateBookingData.TOTAL_PRICE,
        "depositpaid": UpdateBookingData.DEPOSIT_PAID,
        "bookingdates": {
            "checkin": UpdateBookingData.CHECKIN,
            "checkout": UpdateBookingData.CHECKOUT
        },
        "additionalneeds": UpdateBookingData.ADDITIONAL_NEEDS
    }

    # SEND REQUEST
    booking_req = requests.put(
        url=f"{url}/{booking_id}",
        headers=headers,
        data=json.dumps(data)
    )

    # ASSERTIONS
    if assume(booking_req.status_code == StatusCodes.OK):
        json_response = json.loads(booking_req.text)
        assume(json_response['firstname'] == UpdateBookingData.FIRSTNAME)
        assume(json_response['lastname'] == UpdateBookingData.LASTNAME)
        assume(json_response['totalprice'] == UpdateBookingData.TOTAL_PRICE)
        assume(json_response['depositpaid'] == UpdateBookingData.DEPOSIT_PAID)
        assume(json_response['bookingdates']['checkin'] == UpdateBookingData.CHECKIN)
        assume(json_response['bookingdates']['checkout'] == UpdateBookingData.CHECKOUT)
        assume(json_response['additionalneeds'] == UpdateBookingData.ADDITIONAL_NEEDS)
        return booking_id

@mark.dependency(depends=["test_create_bookings"])
def test_partial_update_created_booking():
    """
    Test case to update a booking.
    """
    # GATHER DATA
    url = add_booking_decorator(GlobalConstants.URL)
    booking_id = test_create_bookings()
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Cookie": f"token={test_admin_auth_token_creation()}"
    }
    data = {
        "firstname": UpdateBookingData.FIRSTNAME,
        "lastname": UpdateBookingData.LASTNAME,
    }

    # SEND REQUEST
    booking_req = requests.patch(
        url=f"{url}/{booking_id}",
        headers=headers,
        data=json.dumps(data)
    )

    # ASSERTIONS
    if assume(booking_req.status_code == StatusCodes.OK):
        json_response = json.loads(booking_req.text)
        assume(json_response['firstname'] == UpdateBookingData.FIRSTNAME)
        assume(json_response['lastname'] == UpdateBookingData.LASTNAME)
        assume(json_response['totalprice'] == BookingData.TOTAL_PRICE)
        assume(json_response['depositpaid'] == BookingData.DEPOSIT_PAID)
        assume(json_response['bookingdates']['checkin'] == BookingData.CHECKIN)
        assume(json_response['bookingdates']['checkout'] == BookingData.CHECKOUT)
        assume(json_response['additionalneeds'] == BookingData.ADDITIONAL_NEEDS)
        return booking_id
