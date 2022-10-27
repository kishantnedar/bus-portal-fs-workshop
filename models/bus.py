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
