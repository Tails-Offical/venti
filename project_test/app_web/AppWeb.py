# -*- coding: UTF-8 -*-
import os
from project_test.app_web.controller import controller_test
from project_test.app_web.controller import controller_maintenance

class AppWeb(object):
    def __init__(self):
        pass

    def controller_test(self, stop_event, logger, path):
        url = [
            (r"/", controller_test.Home, {"stop_event": stop_event, "logger": logger}),
            (r"/gtool", controller_test.Gtool, {"stop_event": stop_event, "logger": logger}),
            (r"/gtool/request", controller_test.GtoolRequest, {"stop_event": stop_event, "logger": logger}),
            (r"/.*", controller_test.Reject)
        ]
        template_path = os.path.join(path, "data", "test", "app", "app_web", "view", "template")
        static_path = os.path.join(path, "data", "test", "app", "app_web", "view", "static")
        return {'url':url,
                'template_path':template_path,
                'static_path':static_path
                }

    def controller_demotenance(self, stop_event):
        url = [
            (r"/", controller_maintenance.Home, {"stop_event": stop_event}),
            (r"/.*", controller_maintenance.Reject)
        ]
        return {'url':url
            }
