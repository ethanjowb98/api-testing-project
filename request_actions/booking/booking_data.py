from dataclasses import dataclass

@dataclass
class BookingData:
    FIRSTNAME: str = "Ethan"
    LASTNAME: str = "Hunt"
    TOTAL_PRICE: int = 100
    DEPOSIT_PAID: bool = True
    CHECKIN: str = "2023-10-10"
    CHECKOUT: str = "2023-10-11"
    ADDITIONAL_NEEDS: str = "Breakfast"

@dataclass
class UpdateBookingData:
    FIRSTNAME: str = "John"
    LASTNAME: str = "Wick"
    TOTAL_PRICE: int = 200
    DEPOSIT_PAID: bool = False
    CHECKIN: str = "2023-10-12"
    CHECKOUT: str = "2023-10-13"
    ADDITIONAL_NEEDS: str = "Lunch"
