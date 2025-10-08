# -*- coding: UTF-8 -*-
import os
import asyncio
from tornado.web import Application
from multiprocessing import Process
import uuid
from venti.vlog import Vlog
from project_demo.app_web.controller import controller_login, controller_logout, controller_upload, controller_download, controller_demo1, controller_demo2

class AppWeb:
    def __init__(self, osname, path, venti_plock, venti_pevent, venti_pqueue, venti_pdict):
        self.osname = osname
        self.path = path
        self.venti_plock = venti_plock
        self.venti_pevent = venti_pevent
        self.venti_pqueue = venti_pqueue
        self.venti_pdict = venti_pdict

    async def loop(self):
        web_logger = Vlog.set_logger(os.path.join(self.path, 'data','project_demo','log','app_web.log'))
        hargs = {"osname": self.osname, "path": self.path, "venti_pqueue": self.venti_pqueue, "venti_pdict": self.venti_pdict, "venti_pevent": self.venti_pevent, "venti_plock": self.venti_plock,  "web_logger": web_logger}
        application = Application(
            [
                (r"/login", controller_login.ControllerLogin, hargs),
                (r"/logout", controller_logout.ControllerLogout, hargs),
                (r"/upload", controller_upload.ControllerUpload, hargs),
                (r"/download", controller_download.ControllerDownload, hargs),
                (r"/demo1", controller_demo1.ControllerDemo1, hargs),
                (r"/demo2", controller_demo2.ControllerDemo2, hargs)
            ],
            cookie_secret = str(uuid.uuid4())
        )

        application.listen(9750, max_buffer_size=100*1024**2, max_body_size=5*1024**3)
        loop = asyncio.get_running_loop()
        await loop.run_in_executor(None, self.venti_pevent.wait)

    def run(self):
        asyncio.run(self.loop())

    @staticmethod
    def app(osname, path, processes, venti_plock, venti_pevent, venti_pqueue, venti_pdict):
        aw = AppWeb(osname, path, venti_plock, venti_pevent, venti_pqueue, venti_pdict)
        processes.append(Process(target=aw.run))