import datetime
from uuid import uuid4


class Booking:
    def __init__(self, booked_by, bus_number, _id=None, booked_on=None):
        self._id = _id if _id else uuid4().hex
        self.booked_by = booked_by
        self.bus_number = bus_number
        self.booked_on = booked_on if booked_on else datetime.datetime.now()
        self.booked_by = booked_by
        self.bus_number = bus_number
        if booked_on:
            self.booked_on = booked_on
        else:
            self.booked_on = datetime.datetime.utcnow()
