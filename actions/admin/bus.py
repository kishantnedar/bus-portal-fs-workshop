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
            bus_start=bus['start_location'],
            bus_destination=bus['destination_location'],
            bus_reg_number=bus['bus_reg_number'],
            bus_runs_on=bus.getlist('runs_on'),
            bus_normal_price=float(bus['normal_seat_price']),
            bus_window_price=float(bus['window_seat_price']),
            bus_left=int(bus['seat_count']),
            bus_right=int(bus['seat_count']),
            bus_window_left=int(bus['seat_count']),
            bus_window_right=int(bus['seat_count'])
        )

        MongoRepository(self._mongoclient).insert(
            dictionary=_bus.__dict__, database=self._db, collection='buses')

        # check if start and destination exist in locations collection and add if not
        start_check = MongoRepository(self._mongoclient).check_if_present(
            database='bus-db', collection='locations', query={'location': bus['start_location']})
        destination_check = MongoRepository(self._mongoclient).check_if_present(
            database='bus-db', collection='locations', query={'location': bus['destination_location']})
        if not (start_check and destination_check):
            MongoRepository(self._mongoclient).insert(
                {'location': bus['start_location']}, database=self._db, collection='locations')
            MongoRepository(self._mongoclient).insert(
                {'location': bus['destination_location']}, database=self._db, collection='locations')

    def get_busses(self):
        mongo_busses_object = MongoRepository(self._mongoclient).find_all(
            database=self._db, collection='buses')
        return [Bus(**bus).__dict__ for bus in mongo_busses_object]

    def delete_bus(self, bus_number):
        return MongoRepository(self._mongoclient).delete(database=self._db, collection='buses', query={'_id': bus_number})

    def schedule_bus(self, bus_number, bus_day, bus_leaving_time, bus_arriving_time):
        return MongoRepository(self._mongoclient).update(database=self._db, collection='buses', query={'_id': bus_number}, update={'$push': {bus_day: {'leaving_time': bus_leaving_time, 'arriving_time': bus_arriving_time}}})
