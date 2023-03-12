from typing import Type
from db.interface import Repository
from db.mongo_repository import MongoRepository
from db.mysql_repository import MySqlRepository

class User:
    
    def __init__(self, repository: Type[Repository]) -> None:
        self.__repository = repository
    
    def store_data(self, data: any) -> None:
        self.__repository.insert(data)

    def delete_data(self, data: any) -> None:
        self.__repository.delete(data)

user = User(MySqlRepository())
user.store_data(23)

user = User(MongoRepository())
user.store_data(23)