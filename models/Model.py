
from abc import ABC, abstractmethod

class Model(ABC):
    
    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def delete(self):
        pass