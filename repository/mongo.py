class MongoRepository(object):
    def __init__(self, mongoclient):
        self._mongoclient = mongoclient  # type: ignore

    def insert(self, database, collection, dictionary):
        try:
            self._mongoclient[database][collection].insert_one(dictionary)
        except TypeError:
            raise TypeError('dictionary must be of type dict')

    def find(self, database, collection, query):
        query_result = self._mongoclient[database][collection].find(query)
        if self._mongoclient[database][collection].count_documents(query) == 0:
            raise ValueError('No documents found')
        return [result for result in query_result]

    def find_one(self, database, collection, query):
        return self._mongoclient[database][collection].find_one(query)

    def find_all(self, database, collection):
        documents = self._mongoclient[database][collection].find({})
        return [document for document in documents]

    def find_with_filter(self, database, collection, query, param):
        return self._mongoclient[database][collection].find(query, param)

    def update(self, database, collection, query, update):
        return self._mongoclient[database][collection].update_one(query, update)

    def delete(self, database, collection, query):
        if self._mongoclient[database][collection].count_documents(query) == 0:
            raise ValueError('No document found')
        return self._mongoclient[database][collection].delete_one(query)

    def delete_all(self, database, collection):
        return self._mongoclient[database][collection].delete_many({})

    def count(self, database, collection):
        return self._mongoclient[database][collection].count_documents({})

    def count_query(self, database, collection, query):
        return self._mongoclient[database][collection].count_documents(query)

    def drop(self, database, collection):
        return self._mongoclient[database][collection].drop()
