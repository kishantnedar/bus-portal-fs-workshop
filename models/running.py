from models.bus import Seat


class Running:
    def __init__(self, _id, bus_id, bus_seats, bus_leaving_on, bus_arriving_at):
        self._id = _id
        self.bus_id = bus_id
        if isinstance(bus_seats, int):
            seats = []
            for seat_number in range(1, bus_seats+1):
                seats.append(Seat(seat_number, 'window_left').__dict__)
                seats.append(Seat(seat_number, 'left').__dict__)
                seats.append(Seat(seat_number, 'window_right').__dict__)
                seats.append(Seat(seat_number, 'right').__dict__)
            self.bus_seats = seats
        else:
            self.bus_seats = bus_seats
        self.bus_leaving_on = bus_leaving_on
        self.bus_arriving_at = bus_arriving_at
