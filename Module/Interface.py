from abc import ABC, abstractmethod

class Interface(ABC):

    @abstractmethod
    def all(self):
        pass
    
    @abstractmethod
    def fetch(self):
        pass

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def create(self):
        pass


