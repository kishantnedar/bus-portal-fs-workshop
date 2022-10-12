from models.bus import Bus, Seats, SeatType, Seat


def add_bus(bus):
    bus = Bus(
        bus_number=bus.number,
        bus_name=bus.name,
        bus_capacity=bus.capacity,
        bus_start=bus.start,
        bus_destination=bus.destination,
        bus_seats=build_seats(
            bus.seat_count, bus.normal_seat_price, bus.window_seat_price),
        bus_reg_number=bus.reg_number
    )
    bus.save()
    return bus


def build_seats(number_of_seats, normal_seat_price, window_seat_price):
    seats = Seats()
    seats.window_left = SeatType(
        seat_price=window_seat_price,
        seat_count=number_of_seats,
        seats=[Seat(seat_number=seat_number)
               for seat_number in range(1, number_of_seats+1)]
    )
    seats.window_right = SeatType(
        seat_price=window_seat_price,
        seat_count=number_of_seats,
        seats=[Seat(seat_number=seat_number)
               for seat_number in range(0, number_of_seats+1)]
    )
    seats.left = SeatType(
        seat_price=normal_seat_price,
        seat_count=number_of_seats,
        seats=[Seat(seat_number=seat_number)
               for seat_number in range(0, number_of_seats+1)]
    )
    seats.right = SeatType(
        seat_price=normal_seat_price,
        seat_count=number_of_seats,
        seats=[Seat(seat_number=seat_number)
               for seat_number in range(0, number_of_seats+1)]
    )
    return seats
