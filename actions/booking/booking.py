from jmespath import search
from models.bus import Bus
from repository.mongo import MongoRepository
import pandas as pd

def get_user_request_buses():
    start_location = search['from']
    destination_location = search['to']
    date = search['date']
    day = pd.Timestamp(date).day_name()
