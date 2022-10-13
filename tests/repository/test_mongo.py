import pytest
import mongomock

from repository.mongo_repository import MongoRepository

# from repository.mongo_repository import MongoRepository


class TestMongoRepository:

    def test_find(self):
        data = [{'_id': 1, 'name': 'John', 'age': 25}]
        repo = MongoRepository(mongomock.MongoClient())
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
        repo = MongoRepository(mockdb)
        for dict in data:
            repo.insert(dictionary=dict, database='test', collection='test')
        assert repo.find(query={'_id': 4}, database='test',
                         collection='test') == None

    def test_insert(self):
        repo = MongoRepository(mongomock.MongoClient())
        data = [
            {'_id': 1, 'name': 'John', 'age': 25},
            {'_id': 2, 'name': 'Jane', 'age': 30},
            {'_id': 3, 'name': 'Jack', 'age': 35},
        ]
        for dict in data:
            repo.insert(dictionary=dict, database='test', collection='test')
        assert repo.find(query={}, database='test', collection='test') == data

    def test_insert_not_dict_type(self):
        repo = MongoRepository(mongomock.MongoClient())
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
        repo = MongoRepository(mongomock.MongoClient())
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
        repo = MongoRepository(mongomock.MongoClient())
        for dict in data:
            repo.insert(dictionary=dict, database='test', collection='test')
        assert repo.find_one(
            query={'name': 'Jill'}, database='test', collection='test') == None

    def test_update(repo, data):
        repo.insert(data)
        repo.update(1, {'name': 'John', 'age': 26})
        assert repo.find_one(1) == {'_id': 1, 'name': 'John', 'age': 26}

    def test_update_not_found(repo, data):
        repo.insert(data)
        repo.update(4, {'name': 'John', 'age': 26})
        assert repo.find_one(4) is None

    def test_delete(repo, data):
        repo.insert(data)
        repo.delete(1)
        assert repo.find() == data[1:]

    def test_delete_not_found(repo, data):

        repo.insert(data)
        repo.delete(4)
        assert repo.find() == data

    def test_delete_all(repo, data):
        repo.insert(data)
        repo.delete_all()
        assert repo.find() == []

    def test_count(repo, data):
        repo.insert(data)
        assert repo.count() == 3

    def test_count_empty(repo):
        assert repo.count() == 0

    def test_count_not_found(repo, data):
        repo.insert(data)
        assert repo.count(4) == 0

    def test_count_found(repo, data):
        repo.insert(data)
        assert repo.count(1) == 1

    def test_count_found_multiple(repo, data):
        repo.insert(data)
        repo.insert(data)
        assert repo.count(1) == 2

    # def test_
