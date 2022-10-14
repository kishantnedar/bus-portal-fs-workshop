# from controllers.book import seat_book
from models.bus import Bus
from repository.mongo import MongoRepository
import pandas as pd

def get_user_request_buses(search):
    start_location = search['from']
    destination_location = search['to']
    date = search['date']
    day = pd.Timestamp(date).day_name()
    print(day)
    
    mongo_busses_object = MongoRepository('buses').find({'bus_start': start_location, 'bus_destination': destination_location, 'bus_runs_on': day})
    return [bus for bus in mongo_busses_object]

def get_selected_bus(bus_num):
    mongo_bus_object = MongoRepository('buses').find({'_id': bus_num})
    return [bus for bus in mongo_bus_object]
