from pymongo import MongoClient
from os import environ


class MongoRepository(object):
    def __init__(self, mongoclient):
        self._mongoclient = mongoclient  # type: ignore

    def insert(self, database, collection, dictionary):
        print('inserting document')
        try:
            self._mongoclient[database][collection].insert_one(dictionary)
        except TypeError:
            raise TypeError('dictionary must be of type dict')

    def find(self, database, collection, query):
        query_result = self._mongoclient[database][collection].find(query)
        if self._mongoclient[database][collection].count_documents(query) == 0:
            return None
        return [result for result in query_result]

    def find_one(self, database, collection, query):
        return self._mongoclient[database][collection].find_one(query)

    def find_all(self, database, collection):
        documents = self._mongoclient[database][collection].find({})
        return [document for document in documents]

    def update(self, database, collection, query, bus):
        return self._mongoclient[database][collection].update_one(query, bus)

    def delete(self, database, collection, query):
        return self._mongoclient[database][collection].delete_one(query)

    def delete_all(self, database, collection):
        return self._mongoclient[database][collection].delete_many({})

    def count(self, database, collection):
        return self._mongoclient[database][collection].count_documents({})

    def count_query(self, database, collection, query):
        return self._mongoclient[database][collection].count_documents(query)

    def drop(self, database, collection):
        return self._mongoclient[database][collection].drop()
