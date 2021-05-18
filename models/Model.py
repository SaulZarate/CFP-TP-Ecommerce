
from abc import ABC, abstractmethod

class Model(ABC):
    
    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def delete(self):
        pass