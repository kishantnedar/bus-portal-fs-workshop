from models.bus import Bus
from repository.mongo import MongoRepository


def add_bus(bus):
    _bus = Bus(
        bus_number=bus['bus_number'],
        bus_name=bus['bus_name'],
        bus_capacity=int(bus['seat_count'])*4,
        bus_start=bus['start_location'],
        bus_destination=bus['destination_location'],
        bus_seats=int(bus['seat_count']),
        bus_reg_number=bus['bus_reg_number'],
        bus_normal_seat_price=float(bus['normal_seat_price']),
        bus_window_seat_price=float(bus['window_seat_price'])
    )
    MongoRepository('buses').insert(_bus.__dict__)


def get_busses():
    mongo_object = MongoRepository('buses').find_all()
    print(mongo_object)


def remove_bus(bus_number):
    MongoRepository('buses').delete({'bus_number': bus_number})


{
    "desination_location": "KAK-123",
    "start_location": "KAK-123",

}
