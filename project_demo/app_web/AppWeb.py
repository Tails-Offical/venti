# -*- coding: UTF-8 -*-
import os
import asyncio
from tornado.ioloop import IOLoop
from tornado.web import Application
from tornado.platform.asyncio import AsyncIOMainLoop
from multiprocessing import Process
import uuid
from venti.vlog import Vlog
from project_demo.app_web.controller import controller_login
from project_demo.app_web.controller import controller_user
from project_demo.app_web.controller import controller_logout

class AppWeb:
    def __init__(self, osname, path, venti_plock, venti_pevent, venti_pqueue, venti_pdict):
        self.osname = osname
        self.path = path
        self.venti_plock = venti_plock
        self.venti_pevent = venti_pevent
        self.venti_pqueue = venti_pqueue
        self.venti_pdict = venti_pdict

    def loop(self):
        web_logger = Vlog.set_logger(os.path.join(self.path, 'data','project_demo','log','app_web.log'))
        application = Application(
            [
                (r"/login", controller_login.Login, {"osname": self.osname, "path": self.path, "venti_pqueue": self.venti_pqueue, "venti_pdict": self.venti_pdict, "venti_pevent": self.venti_pevent, "venti_plock": self.venti_plock,  "web_logger": web_logger}),
                (r"/logout", controller_logout.Logout, {"osname": self.osname, "path": self.path, "venti_pqueue": self.venti_pqueue, "venti_pdict": self.venti_pdict, "venti_pevent": self.venti_pevent, "venti_plock": self.venti_plock,  "web_logger": web_logger}),
                (r"/user", controller_user.User, {"osname": self.osname, "path": self.path, "venti_pqueue": self.venti_pqueue, "venti_pdict": self.venti_pdict, "venti_pevent": self.venti_pevent, "venti_plock": self.venti_plock,  "web_logger": web_logger})
            ],
            cookie_secret = str(uuid.uuid4())
        )
        AsyncIOMainLoop().install()
        application.listen(9750)
        def check_stop():
            if self.venti_pevent.is_set():
                IOLoop.current().stop()
            else:
                IOLoop.current().call_later(3, check_stop)
        IOLoop.current().call_later(3, check_stop)
        async def task():
            while True:
                await asyncio.sleep(10)
                web_logger.info("app web task")
        IOLoop.current().spawn_callback(task)
        IOLoop.current().start()

    @staticmethod
    def app(osname, path, processes, venti_plock, venti_pevent, venti_pqueue, venti_pdict):
        aw = AppWeb(osname, path, venti_plock, venti_pevent, venti_pqueue, venti_pdict)
        processes.append(Process(target=aw.loop))