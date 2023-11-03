from configurations.constants import GlobalConstants
from configurations.constants import StatusCodes
from request_actions.booking.booking_data import BookingData
from request_actions.booking.booking_requests import add_booking_decorator
from jsonpath import jsonpath
from pytest import assume, mark
import json
import requests

@mark.dependency()
def test_create_bookings():
    """
    Test case to create a booking.

    Returns:
        int: The booking ID.
    """
    # GATHER DATA
    url = add_booking_decorator(GlobalConstants.URL)
    data = {
        "firstname": BookingData.FIRSTNAME,
        "lastname": BookingData.LASTNAME,
        "totalprice": BookingData.TOTAL_PRICE,
        "depositpaid": BookingData.DEPOSIT_PAID,
        "bookingdates": {
            "checkin": BookingData.CHECKIN,
            "checkout": BookingData.CHECKOUT
        },
        "additionalneeds": BookingData.ADDITIONAL_NEEDS
    }

    # SEND REQUEST
    booking_req = requests.post(url=url, json=data)

    # ASSERTIONS
    if assume(booking_req.status_code == StatusCodes.OK):
        json_response = json.loads(booking_req.text)
        booking_id = jsonpath(json_response, 'bookingid')[0]
        return booking_id
