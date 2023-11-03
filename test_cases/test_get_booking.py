from configurations.constants import StatusCodes
from configurations.constants import GlobalConstants
from request_actions.booking.booking_data import BookingData
from request_actions.booking.booking_requests import add_booking_decorator
from .test_create_booking import test_create_bookings
from jsonpath import jsonpath
from pytest import assume, mark
import requests
import json

@mark.dependency(depends=["test_create_bookings"])
def test_get_booking_id_details():
    """
    Test case to get a booking by ID.

    Returns:
        int: The booking ID.
    """
    # GATHER DATA
    url = add_booking_decorator(GlobalConstants.URL)
    booking_id = test_create_bookings()

    # SEND REQUEST
    booking_req = requests.get(url=f"{url}/{booking_id}")

    # ASSERTIONS
    if assume(booking_req.status_code == StatusCodes.OK):
        json_response = json.loads(booking_req.text)
        assume(json_response['firstname'] == BookingData.FIRSTNAME)
        assume(json_response['lastname'] == BookingData.LASTNAME)
        assume(json_response['totalprice'] == BookingData.TOTAL_PRICE)
        assume(json_response['depositpaid'] == BookingData.DEPOSIT_PAID)
        assume(json_response['bookingdates']['checkin'] == BookingData.CHECKIN)
        assume(json_response['bookingdates']['checkout'] == BookingData.CHECKOUT)
        assume(json_response['additionalneeds'] == BookingData.ADDITIONAL_NEEDS)
        return booking_id
