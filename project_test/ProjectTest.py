# -*- coding: UTF-8 -*-
from tornado.ioloop import IOLoop
from tornado.web import Application
from tornado.platform.asyncio import AsyncIOMainLoop
import os
import asyncio
from venti import vlog
from project_test.app_web.AppWeb import AppWeb
from project_test.app_cron.AppAcron import AppAcron

class ProjectTest(object):
    def __init__(self):
        pass

    def app_web(self, stop_event, path):
        log_file = os.path.join(path, 'data','test','log','app_web.log')
        vv = vlog.Vlog(log_file)
        vcl = vlog.CustomLogger
        logger = vv.logger(vcl)

        try:
            aw = AppWeb()
            config = aw.controller_test(stop_event, logger, path)
            application = Application(
                config["url"],
                template_path = config["template_path"],
                static_path = config["static_path"]
            )
            AsyncIOMainLoop().install()
            application.listen(9750)
            def check_stop():
                if stop_event.is_set():
                    IOLoop.current().stop()
                else:
                    IOLoop.current().call_later(3, check_stop)
            IOLoop.current().call_later(3, check_stop)
            IOLoop.current().start()
        except Exception as e:
            logger.error(e)
        finally:
            pass

    def app_cron(self, stop_event, path):
        log_file = os.path.join(path, 'data','test','log','app_cron.log')
        vv = vlog.Vlog(log_file)
        vcl = vlog.CustomLogger
        logger = vv.logger(vcl)

        try:
            loop = asyncio.get_event_loop()
            loop.run_until_complete(AppAcron(stop_event, logger, path).exe())
        except Exception as e:
            logger.error(e)
        finally:
            pass
