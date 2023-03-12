from .interface import Repository

class MySqlRepository(Repository):
    def insert(self, data) -> None:
         print('Inserting {} on database MySql'.format(data))

    def delete(self, data) -> None:
        print('Deleting {} on database MySql'.format(data))