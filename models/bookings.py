from models.bus import Bus,


class Bookings:
    def __init__(self, _id, running_id, booked_by, seat_price, seat_type, seat_number, booked_on):
        self._id = _id
        self.running_id = running_id
        self.booked_by = booked_by
        self.seat_price = seat_price
        self.seat_type = seat_type
        self.seat_number = seat_number
        self.booked_on = booked_on
