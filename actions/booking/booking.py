
from models.booking import Booking
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
    mongo_bus_object = MongoRepository('buses').find_one({'_id': bus_num})
    return mongo_bus_object


def book_ticket(ticket):
    print(ticket)
    print(f'{ticket["bus_number"]}: {type(ticket["bus_number"])}')
    bus = MongoRepository('buses').find_one(
        {'_id': int(ticket['bus_number'])})
    seats = bus['bus_seats']
    print("_________________________________")
    print(seats)
    for seat in ticket['window_left']:
        seats['window_left']['seats'][int(
            seat)-1]['seat_occupied'] = True
        seats['window_left']['seats'][int(
            seat)-1]['reserved_by'] = ticket['user_id']

    for seat in ticket['window_right']:
        seats['window_right']['seats'][int(
            seat)-1]['seat_occupied'] = True
        seats['window_right']['seats'][int(
            seat)-1]['reserved_by'] = ticket['user_id']

    for seat in ticket['left']:
        seats['left']['seats'][int(
            seat)-1]['seat_occupied'] = True
        seats['left']['seats'][int(
            seat)-1]['reserved_by'] = ticket['user_id']

    for seat in ticket['right']:
        seats['right']['seats'][int(
            seat)-1]['seat_occupied'] = True
        seats['right']['seats'][int(
            seat)-1]['reserved_by'] = ticket['user_id']

    MongoRepository('buses').update(
        {'_id': int(ticket['bus_number'])}, {'$set': {'bus_seats': seats}})
    # booking = Booking()
    MongoRepository('bookings').insert(ticket)
