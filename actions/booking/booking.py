from models.bus import Bus
from repository.mongo import MongoRepository
import pandas as pd

def get_user_request_buses(search):
    start_location = search['from']
    destination_location = search['to']
    date = search['date']
    day = pd.Timestamp(date).day_name()
    
    mongo_busses_object = MongoRepository('buses').find({'bus_start': start_location, 'bus_destination': destination_location, 'bus_runs_on': day})
    return [bus for bus in mongo_busses_object]


