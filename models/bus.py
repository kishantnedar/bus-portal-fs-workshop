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


class Bus:
    def __init__(self, _id, name, start, destination, seat_columns, reg_number, runs_on, window_seat_price, normal_seat_price):
        self._id = int(_id)
        self.name = name
        self.reg_number = reg_number
        self.start = start
        self.destination = destination
        self.runs_on = runs_on
        self.seat_columns = seat_columns
        self.window_seat_price = window_seat_price
        self.normal_seat_price = normal_seat_price
