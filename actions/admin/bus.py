from models.bus import Bus
from repository.mongo import MongoRepository
from pymongo import MongoClient
from os import environ
from models.schedule import Schedule


class AdminActions:
    def __init__(self):
        self._mongo = MongoRepository(MongoClient(host=environ.get(
            'DB_HOST'), username=environ.get('DB_UNAME'), password=environ.get('DB_PASSWD')))
        self._db = environ.get('DB_NAME')

    def add_bus(self, bus):
        _bus = Bus(
            _id=bus['bus_number'],
            name=bus['bus_name'],
            start=bus['start_location'],
            destination=bus['destination_location'],
            reg_number=bus['bus_reg_number'],
            normal_seat_price=float(bus['normal_seat_price']),
            window_seat_price=float(bus['window_seat_price']),
            runs_on=bus.getlist('runs_on'),
            seat_columns=bus['seat_columns']
        ).__dict__
        return self._mongo.insert(database=self._db, collection='buses', dictionary=_bus)

    def get_busses(self):
        mongo_busses_object = self._mongo.find_all(
            database=self._db, collection='buses')
        return [Bus(**bus).__dict__ for bus in mongo_busses_object]

    def delete_bus(self, bus_number):
        return self._mongo.delete(query={'_id': bus_number}, database=self._db, collection='buses')

    def schedule_bus(self, schedule):
        _schedule = Schedule(
            bus_number=int(schedule['bus_number']), scheduled_on=schedule['date'],  departure_time=schedule['start_time'], arrival_time=schedule['end_time'], seats=int(float(schedule['seat_count'])), normal_seat_price=schedule['normal_seat_price'], window_seat_price=schedule['window_seat_price'], seat_columns=int(float(schedule['seat_count']))).__dict__
        return self._mongo.insert(database=self._db, collection='schedule', dictionary=_schedule)
