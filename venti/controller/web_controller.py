from tornado.web import Application
import os
from venti.utils.handler.timing_handler import timeit
from venti.utils.vnet import AsyncHandler

class HelloWebController:
    def __init__(self, ij):
        '''
        1 将从main.py之中的依赖字典传递至此
        2 取出并实例化字典中的对象，并将依赖继续传递给service层
        '''
        self.ij = ij['HelloWebServiceImplement'](ij)

    @timeit
    def hello(self):
        print(self.ij.hello())
        return 'Hello WebController'

class WebController(AsyncHandler):
    def initialize(self, ij):
        self.ij = ij['WebServiceImplement'](ij)

    async def get(self):
        print(self.ij.get_data())
        self.render('home.html')
        

def make_app(ij):
    return Application([
        (r"/",  WebController,dict(ij=ij)),
    ], 
    template_path=os.path.join(os.getcwd(),"resource", "template"),
    static_path=os.path.join(os.getcwd(),"resource", "template", "static")
    )
