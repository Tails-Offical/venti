# -*- coding: UTF-8 -*-
import os
import asyncio
from tornado.ioloop import IOLoop
from tornado.web import Application
from tornado.platform.asyncio import AsyncIOMainLoop
from venti.vlog import Vlog
from project_demo.app_web.controller import controller_user

class AppWeb:
    def __init__(self, venti_queue, venti_dict, venti_event, venti_lock, path, stype):
        self.url = []
        self.venti_queue = venti_queue
        self.venti_dict = venti_dict
        self.venti_event = venti_event
        self.venti_lock = venti_lock
        self.path = path
        self.stype = stype
        self.vlog = Vlog()
        self.app_web_logger = self.vlog.set_logger(os.path.join(self.path, 'data','project_demo','log','app_web.log'))

    def controller_user(self):
        return [
            (r"/user", controller_user.User, {"venti_queue": self.venti_queue, "venti_dict": self.venti_dict, "venti_event": self.venti_event, "venti_lock": self.venti_lock, "path": self.path, "stype": self.stype, "app_web_logger": self.app_web_logger})
        ]

    def controller(self):
        self.controller_user()
        try:
            application = Application(
                self.controller_user()
            )
            AsyncIOMainLoop().install()
            application.listen(9750)
            def check_stop():
                if self.venti_event.is_set():
                    IOLoop.current().stop()
                else:
                    IOLoop.current().call_later(3, check_stop)
            IOLoop.current().call_later(3, check_stop)
            async def async_task():
                while True:
                    await asyncio.sleep(6)
                    self.app_web_logger.info("async_task")
            IOLoop.current().spawn_callback(async_task)
            IOLoop.current().start()
        except Exception as e:
            self.app_web_logger.error(e)

