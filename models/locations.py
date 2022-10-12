from mongoengine import Document, StringField, IntField, DateTimeField, ReferenceField, ListField, EmbeddedDocumentField


class Locations(Document):
    meta = {'collection': 'locations'}
    location = StringField(required=True)
