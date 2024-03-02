from abc import ABC, abstractmethod

class WebServiceInterface(ABC):
    @abstractmethod
    def __init__(self, ij):
        pass

    @abstractmethod
    def get_data(self):
        pass
