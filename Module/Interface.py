from abc import ABC, abstractmethod

class Interface(ABC):

    @abstractmethod
    def read_all(self):
        pass
    
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def create(self):
        pass