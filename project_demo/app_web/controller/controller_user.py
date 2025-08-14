# -*- coding: UTF-8 -*-
from tornado.web import RequestHandler
from project_demo.app_web.service.service_user import ServiceUser

class BaseHandler(RequestHandler):
    def initialize(self, venti_queue, venti_dict, venti_event, venti_lock, path, stype, app_web_logger):
        self.venti_queue = venti_queue
        self.venti_dict = venti_dict
        self.venti_event = venti_event
        self.venti_lock = venti_lock
        self.path = path
        self.stype = stype
        self.app_web_logger = app_web_logger
        self.su = ServiceUser(self.app_web_logger)

class User(BaseHandler):
    async def get(self):
        self.write(str(self.su.get_user()))
