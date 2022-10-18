import pytest
import mongomock

from repository.mongo import MongoRepositoryNew

# from repository.mongo_repository import MongoRepository


class TestMongoRepository():

    def test_find(self):
        data = [{'_id': 1, 'name': 'John', 'age': 25}]
        repo = MongoRepositoryNew(mongomock.MongoClient())
        for dict in data:
            repo.insert(dictionary=dict, database='test', collection='test')
        assert repo.find(query={'_id': 1}, database='test',
                         collection='test') == data

    def test_find_not_found(self):
        data = [
            {'_id': 1, 'name': 'John', 'age': 25},
            {'_id': 2, 'name': 'Jane', 'age': 30},
            {'_id': 3, 'name': 'Jack', 'age': 35},
        ]
        mockdb = mongomock.MongoClient()
        repo = MongoRepositoryNew(mockdb)
        for dict in data:
            repo.insert(dictionary=dict, database='test', collection='test')
        assert repo.find(query={'_id': 4}, database='test',
                         collection='test') == None

    def test_insert(self):
        repo = MongoRepositoryNew(mongomock.MongoClient())
        data = [
            {'_id': 1, 'name': 'John', 'age': 25},
            {'_id': 2, 'name': 'Jane', 'age': 30},
            {'_id': 3, 'name': 'Jack', 'age': 35},
        ]
        for dict in data:
            repo.insert(dictionary=dict, database='test', collection='test')
        assert repo.find(query={}, database='test', collection='test') == data

    def test_insert_not_dict_type(self):
        repo = MongoRepositoryNew(mongomock.MongoClient())
        with pytest.raises(TypeError):
            repo.insert(dictionary=[1, 2, 3],
                        database='test', collection='test')

    def test_find_one(self):
        data = [
            {'_id': 1, 'name': 'John', 'age': 25},
            {'_id': 2, 'name': 'Jane', 'age': 30},
            {'_id': 3, 'name': 'Jack', 'age': 35},
            {'_id': 4, 'name': 'Jack', 'age': 40},
        ]
        repo = MongoRepositoryNew(mongomock.MongoClient())
        for dict in data:
            repo.insert(dictionary=dict, database='test', collection='test')
        assert repo.find_one(
            query={'name': 'Jack'}, database='test', collection='test') == data[2]

    def test_find_one_not_found(self):
        data = [
            {'_id': 1, 'name': 'John', 'age': 25},
            {'_id': 2, 'name': 'Jane', 'age': 30},
            {'_id': 3, 'name': 'Jack', 'age': 35},
            {'_id': 4, 'name': 'Jack', 'age': 40},
        ]
        repo = MongoRepositoryNew(mongomock.MongoClient())
        for dict in data:
            repo.insert(dictionary=dict, database='test', collection='test')
        assert repo.find_one(
            query={'name': 'Jill'}, database='test', collection='test') == None

    def test_update(self):
        data = [
            {'_id': 1, 'name': 'John', 'age': 25},
            {'_id': 2, 'name': 'Jane', 'age': 30},
            {'_id': 3, 'name': 'Jack', 'age': 35},
            {'_id': 4, 'name': 'Jack', 'age': 40},
        ]
        repo = MongoRepositoryNew(mongomock.MongoClient())
        for dict in data:
            repo.insert(dictionary=dict, database='test', collection='test')
        repo.update(query={'_id': 1}, update={'$set': {'age': 26}},
                    database='test', collection='test')
        assert repo.find_one(query={'_id': 1}, database='test',
                             collection='test') == {'_id': 1, 'name': 'John', 'age': 26}

    def test_update_not_found(self):
        data = [
            {'_id': 1, 'name': 'John', 'age': 25},
            {'_id': 2, 'name': 'Jane', 'age': 30},
            {'_id': 3, 'name': 'Jack', 'age': 35},
            {'_id': 4, 'name': 'Jack', 'age': 40},
        ]
        repo = MongoRepositoryNew(mongomock.MongoClient())
        for dict in data:
            repo.insert(dictionary=dict, database='test', collection='test')
        repo.update(query={'_id': 5}, update={'$set': {'age': 26}},
                    database='test', collection='test')
        assert repo.find_one(query={'_id': 5}, database='test',
                             collection='test') == None

    def test_delete(self):
        data = [
            {'_id': 1, 'name': 'John', 'age': 25},
            {'_id': 2, 'name': 'Jane', 'age': 30},
            {'_id': 3, 'name': 'Jack', 'age': 35},
            {'_id': 4, 'name': 'Jack', 'age': 40},
        ]
        repo = MongoRepositoryNew(mongomock.MongoClient())
        for dict in data:
            repo.insert(dictionary=dict, database='test', collection='test')
        repo.delete(database='test', collection='test', query={'_id': 1})
        assert repo.find(database='test', collection='test',
                         query={}) == data[1:]

    def test_delete_not_found(self):
        data = [
            {'_id': 1, 'name': 'John', 'age': 25},
            {'_id': 2, 'name': 'Jane', 'age': 30},
            {'_id': 3, 'name': 'Jack', 'age': 35},
            {'_id': 4, 'name': 'Jack', 'age': 40},
        ]
        repo = MongoRepositoryNew(mongomock.MongoClient())
        for dict in data:
            repo.insert(dictionary=dict, database='test', collection='test')
        with pytest.raises(ValueError):
            repo.delete(database='test', collection='test', query={'_id': 5})

    def test_delete_all(self):
        data = [
            {'_id': 1, 'name': 'John', 'age': 25},
            {'_id': 2, 'name': 'Jane', 'age': 30},
            {'_id': 3, 'name': 'Jack', 'age': 35},
            {'_id': 4, 'name': 'Jack', 'age': 40},
        ]
        repo = MongoRepositoryNew(mongomock.MongoClient())
        for dict in data:
            repo.insert(dictionary=dict, database='test', collection='test')
        repo.delete_all(database='test', collection='test')
        assert repo.find(database='test', collection='test', query={}) == None

    def test_count(self):
        data = [
            {'_id': 1, 'name': 'John', 'age': 25},
            {'_id': 2, 'name': 'Jane', 'age': 30},
            {'_id': 3, 'name': 'Jack', 'age': 35},
            {'_id': 4, 'name': 'Jack', 'age': 40},
        ]
        repo = MongoRepositoryNew(mongomock.MongoClient())
        for dict in data:
            repo.insert(dictionary=dict, database='test', collection='test')
        assert repo.count(database='test', collection='test') == 4

    def test_count_empty(self):
        repo = MongoRepositoryNew(mongomock.MongoClient())
        assert repo.count(database='test', collection='test') == 0

    def test_count_query_not_found(self):
        data = [
            {'_id': 1, 'name': 'John', 'age': 25},
            {'_id': 2, 'name': 'Jane', 'age': 30},
            {'_id': 3, 'name': 'Jack', 'age': 35},
            {'_id': 4, 'name': 'Jack', 'age': 40},
        ]
        repo = MongoRepositoryNew(mongomock.MongoClient())
        for dict in data:
            repo.insert(dictionary=dict, database='test', collection='test')
        assert repo.count_query(database='test', collection='test', query={
                                'name': "Jenny"}) == 0

    def test_count_query(self):
        data = [
            {'_id': 1, 'name': 'John', 'age': 25},
            {'_id': 2, 'name': 'Jane', 'age': 30},
            {'_id': 3, 'name': 'Jack', 'age': 35},
            {'_id': 4, 'name': 'Jack', 'age': 40},
        ]
        repo = MongoRepositoryNew(mongomock.MongoClient())
        for dict in data:
            repo.insert(dictionary=dict, database='test', collection='test')
        assert repo.count_query(database='test', collection='test', query={
                                'name': "Jack"}) == 2

    def test_count_query_empty(self):
        repo = MongoRepositoryNew(mongomock.MongoClient())
        assert repo.count_query(database='test', collection='test', query={
                                'name': "Jack"}) == 0
