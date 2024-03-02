from abc import ABC, abstractmethod

class WebRepositoryInterface(ABC):
    @abstractmethod
    def get_data(self):
        pass
