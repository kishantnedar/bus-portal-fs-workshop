from models.bus import Bus
from repository.mongo_repository import MongoRepository
from os import environ
from pymongo import MongoClient


class BusActions:
    def __init__(self):
        self._mongoclient = mongo_client = MongoClient(
            environ.get('DB_HOST'), username=environ.get("DB_UNAME"), password=environ.get("DB_PASSWD"))
        self._db = environ.get('DB_NAME')

    def add_bus(self, bus):
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
        MongoRepository(self._mongoclient).insert(
            _bus.__dict__, database=self._db, collection='buses')

    def get_busses(self):
        mongo_busses_object = MongoRepository(self._mongoclient).find_all(
            database=self._db, collection='buses')
        return [Bus(**bus).__dict__ for bus in mongo_busses_object]

    def delete_bus(self, bus_number):
        return MongoRepository(self._mongoclient).delete(database=self._db, collection='buses', query={'_id': bus_number})
