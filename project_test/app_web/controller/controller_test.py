# -*- coding: UTF-8 -*-
from tornado.web import RequestHandler

class Home(RequestHandler):
    def initialize(self, stop_event, logger):
        self.stop_event = stop_event
        self.logger = logger

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "Content-Type, Authorization")  
        self.set_header("Access-Control-Allow-Methods", "GET, POST, PUT, OPTIONS")  

    def options(self):
        self.set_status(204)
        self.finish()

    async def get(self):
        self.render('home.html')

class Gtool(RequestHandler):
    def initialize(self, stop_event, logger):
        self.stop_event = stop_event
        self.logger = logger
    
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "Content-Type, Authorization")  
        self.set_header("Access-Control-Allow-Methods", "GET, POST, PUT, OPTIONS")  

    def options(self):
        self.set_status(204)
        self.finish()

    async def get(self):
        self.render('gtool/gtool.html')

class GtoolRequest(RequestHandler):
    def initialize(self, stop_event, logger):
        self.stop_event = stop_event
        self.logger = logger

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "Content-Type, Authorization")  
        self.set_header("Access-Control-Allow-Methods", "GET, POST, PUT, OPTIONS")  

    def options(self):
        self.set_status(204)
        self.finish()

    async def get(self):
        self.render('gtool/request.html')

class Reject(RequestHandler):
    async def get(self):
        self.write("reject")

    async def post(self):
        self.finish("reject")

    async def put(self):
        self.finish("reject")

    async def delete(self):
        self.finish("reject")