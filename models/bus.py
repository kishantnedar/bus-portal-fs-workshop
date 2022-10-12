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
    def __init__(self, bus_number, bus_name, bus_capacity, bus_start, bus_destination, bus_seats, bus_reg_number, bus_normal_seat_price, bus_window_seat_price):
        self.bus_number = bus_number
        self.bus_name = bus_name
        self.bus_reg_number = bus_reg_number
        self.bus_capacity = bus_capacity
        self.bus_start = bus_start
        self.bus_destination = bus_destination
        if isinstance(bus_seats, int):
            self.bus_seats = Seats(
                seat_count=bus_seats, normal_price=bus_normal_seat_price, window_price=bus_window_seat_price).__dict__
        else:
            self.bus_seats = bus_seats
