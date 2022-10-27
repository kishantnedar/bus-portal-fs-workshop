from uuid import uuid4
from datetime import datetime


class Seat:
    def __init__(self, seat_number):
        self.seat_number = seat_number
        self.seat_occupied = False
        self.reserved_by = None


class SeatType:
    def __init__(self, count, price):
        self.seat_price = price
        self.seat_count = count
        self.seats = [Seat(seat_number=seat_number).__dict__
                      for seat_number in range(1, count+1)]


class Seats:
    def __init__(self, window_price, normal_price, seat_count):
        self.window_left = SeatType(seat_count, window_price).__dict__
        self.window_right = SeatType(seat_count, window_price).__dict__
        self.left = SeatType(seat_count, normal_price).__dict__
        self.right = SeatType(seat_count, normal_price).__dict__


class Schedule:
    def __init__(self, bus_number, scheduled_on, departure_time, arrival_time, seats, normal_seat_price, window_seat_price, seat_columns, _id=None):
        self._id = _id if _id else uuid4().hex
        self.bus_number = bus_number
        self.scheduled_on = scheduled_on
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        if isinstance(seats, int):
            self.seats = Seats(
                seat_count=seats, normal_price=int(normal_seat_price), window_price=int(window_seat_price)).__dict__
        else:
            self.bus_seats = seats
        self.normal_seat_price = normal_seat_price
        self.window_seat_price = window_seat_price
        self.seat_columns = seat_columns
