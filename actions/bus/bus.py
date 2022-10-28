from repository.mongo import MongoRepository
from os import environ
from pymongo import MongoClient


class BusActions:
    def __init__(self):
        self._mongo = MongoRepository(MongoClient(host=environ.get(
            'DB_HOST'), username=environ.get('DB_UNAME'), password=environ.get('DB_PASSWD')))
        self._db = environ.get('DB_NAME')

    def get_bus(self, bus_number):
        return self._mongo.find_one(database=self._db, collection='buses', query={'_id': bus_number})

    def get_buses(self):
        return self._mongo.find(database=self._db, collection='buses', query={})
    
    def get_bus_schedules(self, bus_number):
        try:
            return self._mongo.find(database=self._db, collection='schedule', query={'bus_number': bus_number})
        except ValueError as e:
            return None
