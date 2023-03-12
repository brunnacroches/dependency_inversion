from abc import ABC, abstractmethod

class Repository(ABC):
    
    @abstractmethod
    def insert(self, data) -> None:
        pass
        # print('Inserting {} on database MySql'.format(data))

    @abstractmethod 
    def delete(self, data) -> None:
        pass
        # print('Deleting {} on database MySql'.format(data))