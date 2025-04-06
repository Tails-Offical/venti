# -*- coding: UTF-8 -*-
from tornado.web import RequestHandler

class Home(RequestHandler):
    def initialize(self, parameter):
        self.parameter = parameter

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "Content-Type, Authorization")  
        self.set_header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS")  

    def options(self):
        self.set_status(204)
        self.finish()

    async def get(self):
        self.finish("Website maintenance in progress")

    async def post(self):
        self.finish("Website maintenance in progress")

    async def put(self):
        self.finish("Website maintenance in progress")

    async def delete(self):
        self.finish("Website maintenance in progress")

class Reject(RequestHandler):
    async def get(self):
        self.finish("reject")

    async def post(self):
        self.finish("reject")

    async def put(self):
        self.finish("reject")

    async def delete(self):
        self.finish("reject")