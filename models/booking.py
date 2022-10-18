import datetime
from uuid import uuid4


class Booking:
    def __init__(self, booked_by, bus_number, booked_tickets, booked_date, _id=None, booked_on=None):
        self._id = _id if _id else uuid4().hex
        self.booked_by = booked_by
        self.bus_number = bus_number
        self.booked_on = booked_on if booked_on else datetime.datetime.now()
        self.booked_tickets = booked_tickets
        self.booked_date = booked_date
