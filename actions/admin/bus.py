from models.bus import Bus
from repository.mongo import MongoRepository


def add_bus(bus):
    _bus = Bus(
        bus_number=bus['number'],
        bus_name=bus['name'],
        bus_capacity=bus['seat_count']*4,
        bus_start=bus['start'],
        bus_destination=bus['destination'],
        bus_seats=bus['seat_count'],
        bus_reg_number=bus['reg_number'],
        bus_normal_seat_price=bus['normal_seat_price'],
        bus_window_seat_price=bus['window_seat_price']
    )
    # print(_bus.__dict__)
    MongoRepository('buses').insert(_bus.__dict__)


def get_busses():
    mongo_object = MongoRepository('buses').find_all()
    print(mongo_object)


def remove_bus(bus_number):
    MongoRepository('buses').delete({'bus_number': bus_number})
