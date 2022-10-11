from mongoengine import Document, StringField, IntField, DateTimeField, ListField, EmbeddedDocumentField, BooleanField, ReferenceField
from datetime import datetime


class Seat(Document):
    seat_number = StringField(required=True, unique=True)
    seat_occupied = BooleanField(required=True, default=False)
    occupied_by = ReferenceField('User', required=False)


class SeatType(Document):
    seat_price = IntField(required=True)
    seat_count = IntField(required=True)
    seats = ListField(EmbeddedDocumentField(Seat))


class Seats(Document):
    window_left = EmbeddedDocumentField(SeatType)
    window_right = EmbeddedDocumentField(SeatType)
    left = EmbeddedDocumentField(SeatType)
    right = EmbeddedDocumentField(SeatType)


class Bus(Document):
    meta = {
        'collection': 'buses'
    }
    bus_number = StringField(required=True, unique=True)
    bus_name = StringField(required=True)
    bus_capacity = IntField(required=True)
    bus_start = StringField(required=True)
    bus_destination = StringField(required=True)
    bus_seats = EmbeddedDocumentField(Seats)
    bus_created = DateTimeField(required=True, default=datetime.now())
    bus_updated = DateTimeField(required=True, default=datetime.now())

    def __repr__(self):
        return self.bus_name

    def to_json(self):
        return {
            'bus_number': self.bus_number,
            'bus_name': self.bus_name,
            'bus_capacity': self.bus_capacity,
            'bus_start': self.bus_start,
            'bus_destination': self.bus_destination,
            'bus_seats': self.bus_seats,
            'bus_created': self.bus_created,
            'bus_updated': self.bus_updated
        }
