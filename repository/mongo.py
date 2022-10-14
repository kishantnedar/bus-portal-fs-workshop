from pymongo import MongoClient
from os import environ


class MongoRepository(object):
    def __init__(self, mongo_collection):
        mongoclient = MongoClient(
            environ.get('DB_HOST'), username=environ.get("DB_UNAME"), password=environ.get("DB_PASSWD"))
        db = mongoclient[environ.get('DB_NAME')]  # type: ignore
        self._collection = db[mongo_collection]

    def insert(self, doc):
        print('inserting document')
        self._collection.insert_one(doc)

    def find(self, query):
        return self._collection.find(query)

    def find_with_filter(self, query, param):
        return self._collection.find(query, param)

    def find_one(self, query):
        return self._collection.find_one(query)

    def find_all(self):
        return self._collection.find()

    def update(self, query, bus):
        return self._collection.update_one(query, bus)

    def delete(self, query):
        return self._collection.delete_one(query)

    def delete_all(self):
        return self._collection.delete_many({})

    def count(self):
        return self._collection.count_documents({})

    def count_query(self, query):
        return self._collection.count_documents(query)

    def drop(self):
        return self._collection.drop()
