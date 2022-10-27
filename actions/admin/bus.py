from models.bus import Bus
from repository.mongo import MongoRepository
from pymongo import MongoClient
from os import environ


class AdminActions:
    def __init__(self):
        self._mongo = MongoRepository(MongoClient(host=environ.get(
            'DB_HOST'), username=environ.get('DB_UNAME'), password=environ.get('DB_PASSWD')))
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
        ).__dict__
        return self._mongo.insert(database=self._db, collection='buses', dictionary=_bus)

    def get_busses(self):
        mongo_busses_object = self._mongo.find_all(
            database=self._db, collection='buses')
        return [Bus(**bus).__dict__ for bus in mongo_busses_object]

    def get_selected_bus(self, bus_num):
        mongo_bus_object = self._mongo.find_one(
            database=self._db, collection='buses', query={'_id': bus_num})
        return mongo_bus_object

    def delete_bus(self, bus_number):
        return self._mongo.delete(query={'_id': bus_number}, database=self._db, collection='buses')
