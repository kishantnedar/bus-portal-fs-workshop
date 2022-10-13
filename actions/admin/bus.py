from models.bus import Bus
from repository.mongo import MongoRepository


def add_bus(bus):
    _bus = Bus(
        _id=bus['bus_number'],
        bus_name=bus['bus_name'],
        bus_capacity=int(bus['seat_count'])*4,
        bus_start=bus['start_location'],
        bus_destination=bus['destination_location'],
        bus_seats=int(bus['seat_count']),
        bus_reg_number=bus['bus_reg_number'],
        bus_normal_seat_price=float(bus['normal_seat_price']),
        bus_window_seat_price=float(bus['window_seat_price']),
        bus_runs_on=bus.getlist('runs_on')
    )
    MongoRepository('buses').insert(_bus.__dict__)


def get_busses():
    mongo_busses_object = MongoRepository('buses').find_all()
    return [Bus(**bus).__dict__ for bus in mongo_busses_object]


def remove_bus(bus_number):
    MongoRepository('buses').delete({'bus_number': bus_number})
