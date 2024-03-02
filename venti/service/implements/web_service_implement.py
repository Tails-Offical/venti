from venti.service.interfaces.web_service_interface import WebServiceInterface
from venti.utils.handler.timing_handler import timeit

class HelloWebServiceImplement:
    def __init__(self, ij):
        # 实例化Repository层实现类HelloWebRepositoryImplement
        self.ij = ij['HelloWebRepositoryImplement']()

    @timeit
    def hello(self):
        print(self.ij.hello())
        return 'Hello WebServiceImplement'

class WebServiceImplement(WebServiceInterface):
    def __init__(self, ij):
        self.ij = ij['WebRepositoryImplement']()

    def get_data(self):
        return self.ij.get_data()

