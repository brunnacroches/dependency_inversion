from .interface import Repository

class MongoRepository(Repository):
    def insert(self, data) -> None:
         print('Inserting {} on database Mongo'.format(data))

    def delete(self, data) -> None:
        print('Deleting {} on database Mongo'.format(data))