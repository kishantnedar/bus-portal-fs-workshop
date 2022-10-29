from models.booking import Booking
from repository.mongo import MongoRepository
from os import environ
from pymongo import MongoClient
from util.date_utils import get_day_name


class BookingActions:
    def __init__(self):
        self._mongo = MongoRepository(MongoClient(host=environ.get(
            'DB_HOST'), username=environ.get('DB_UNAME'), password=environ.get('DB_PASSWD')))
        self._db = environ.get('DB_NAME')

    def get_user_request_buses(self, search):
        start_location = search['from']
        destination_location = search['to']
        date = search['date']
        day = get_day_name(date)
        try:
            mongo_busses_object = self._mongo.find(database=self._db, collection='buses',
                                                   query={'start': start_location, 'destination': destination_location, 'runs_on': day})
            mongo_scheduled_object = self._mongo.find(
                database=self._db, collection='schedule', query={'bus_number': {'$in': [bus['_id'] for bus in mongo_busses_object]}, 'scheduled_on': search['date']})
        except ValueError as e:
            return None
        return [bus for bus in mongo_scheduled_object]

    def get_selected_schedule(self, schedule):
        mongo_schedule_object = self._mongo.find_one(
            database=self._db, collection='schedule', query={'_id': schedule})
        return mongo_schedule_object

    def book_ticket(self, ticket):
        bus = self._mongo.find_one(database=self._db, collection='schedule', query={
            '_id': ticket['schedule_id']})
        seats = bus['seats']
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

        self._mongo.update(database=self._db, collection='schedule', query={
                           '_id': ticket['schedule_id']}, update={'$set': {'seats': seats}})
        booking = Booking(
            booked_by=ticket['user_id'], bus_number=ticket['bus_number'], schedule_id=ticket['schedule_id'], booked_tickets={'window_left': ticket['window_left'], 'window_right': ticket['window_right'], 'left': ticket['left'], 'right': ticket['right']}, booked_date=ticket['booked_date'], booking_price=ticket['booking_price'])
        self._mongo.insert(database=self._db,
                           collection='bookings', dictionary=booking.__dict__)
        return booking

    def get_locations(self):
        return self._mongo.find_with_filter(database=self._db, collection='buses', query={}, param={"_id": 0, "start": 1, "destination": 1})

    def get_bookings(self, user_id):
        bookings = [Booking(**booking)
                    for booking in self._mongo.find(database=self._db, collection='bookings', query={'booked_by': user_id})]
        return bookings

    def get_booking(self, booking_id):
        booking = Booking(
            **self._mongo.find_one(database=self._db, collection='bookings', query={'_id': booking_id}))
        return booking

    def get_bookings_by_bus(self, bus_id):
        booking = [Booking(**booking) for booking in self._mongo.find(
            database=self._db, collection='bookings', query={"bus_number": bus_id})]
        return booking

    def get_bookings_by_schedule(self, schedule_id):
        try:
            return [Booking(**booking) for booking in self._mongo.find(
            database=self._db, collection='bookings', query={"schedule_id": schedule_id})]
        except ValueError as e:
            return None

    def delete_booking(self, booking_id):
        self._mongo.delete(database=self._db, collection='bookings', query={
                           '_id': booking_id})

    def booking_cancellation(self, booking_id, booked_by):
        id_data = self._mongo.find_one(database=self._db, collection='bookings', query={
            '_id': booking_id, 'booked_by': booked_by})
        booked_tickets = id_data['booked_tickets']

        bus_schedule = self._mongo.find_one(database=self._db, collection='schedule', query={
            '_id': id_data['schedule_id']})
        seats = bus_schedule['seats']
        # left window seats cancellation code

        if len(booked_tickets['window_left']) > 0:
            occupied_seats = booked_tickets['window_left']

            for n in occupied_seats:
                n = int(n)
                seats["window_left"]["seats"][n-1]["seat_occupied"] = False
                seats["window_left"]["seats"][n-1]["reserved_by"] = None

            self._mongo.update(database=self._db, collection='schedule', query={
                '_id': id_data['schedule_id']}, update={'$set': {'seats': seats}})

         # right window seats cancellation code
        if len(booked_tickets['window_right']) > 0:
            occupied_seats = booked_tickets['window_right']

            for n in occupied_seats:
                n = int(n)
                seats["window_right"]["seats"][n-1]["seat_occupied"] = False
                seats["window_right"]["seats"][n-1]["reserved_by"] = None

            self._mongo.update(database=self._db, collection='schedule', query={
                '_id': id_data['schedule_id']}, update={'$set': {'seats': seats}})

        # left seats cancellation code
        if len(booked_tickets['left']) > 0:
            occupied_seats = booked_tickets['left']

            for n in occupied_seats:
                n = int(n)
                seats["left"]["seats"][n-1]["seat_occupied"] = False
                seats["left"]["seats"][n-1]["reserved_by"] = None

            self._mongo.update(database=self._db, collection='schedule', query={
                '_id': id_data['schedule_id']}, update={'$set': {'seats': seats}})

        # right seats cancellation code

        if len(booked_tickets['right']) > 0:
            occupied_seats = booked_tickets['right']

            for n in occupied_seats:
                n = int(n)
                seats["right"]["seats"][n-1]["seat_occupied"] = False
                seats["right"]["seats"][n-1]["reserved_by"] = None

            self._mongo.update(database=self._db, collection='schedule', query={
                '_id': id_data['schedule_id']}, update={'$set': {'seats': seats}})

        self._mongo.delete(database=self._db, collection='bookings', query={
            '_id': booking_id})
        return booking_id
