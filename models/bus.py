from datetime import datetime


class Seat:
    def __init__(self, seat_number, seat_type):
        self.seat_number = seat_type + str(seat_number)
        self.seat_occupied = False
        self.seat_type = seat_type


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
    def __init__(self, _id, bus_name, bus_start, bus_destination, bus_reg_number, bus_runs_on, bus_normal_price, bus_window_price, bus_window_left, bus_window_right, bus_left, bus_right):
        self._id = int(_id)
        self.bus_name = bus_name
        self.bus_start = bus_start
        self.bus_destination = bus_destination
        self.bus_reg_number = bus_reg_number
        self.bus_runs_on = bus_runs_on
        self.bus_normal_price = bus_normal_price
        self.bus_window_price = bus_window_price
        self.bus_window_left = bus_window_left
        self.bus_window_right = bus_window_right
        self.bus_left = bus_left
        self.bus_right = bus_right
        # if isinstance(bus_seats, int):
        #     for seat_number in range(1, bus_seats+1):
        #         seats.append(Seat(seat_number, 'window_left').__dict__)
        #     seats = []
        #         seats.append(Seat(seat_number, 'window_right').__dict__)
        #     self.bus_seats = bus_seats

        #         seats.append(Seat(seat_number, 'left').__dict__)
        #         seats.append(Seat(seat_number, 'right').__dict__)
        #     self.bus_seats = seats
        # else:
