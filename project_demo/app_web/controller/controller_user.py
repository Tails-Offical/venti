# -*- coding: UTF-8 -*-
import tornado.web
from project_demo.app_web.controller.controller_base import BaseHandler
from project_demo.app_web.service.service_user import ServiceUser

class User(BaseHandler):
    def initialize(self, osname, path, venti_plock, venti_pevent, venti_pqueue, venti_pdict, web_logger):
        super().initialize(osname, path, venti_plock, venti_pevent, venti_pqueue, venti_pdict, web_logger)
        self.su = ServiceUser(web_logger)

    @tornado.web.authenticated
    async def post(self):
        current_user = self.get_current_user()
        username = current_user.get("name")
        userid = current_user.get("userid")
        self.write({
            "msg": "success", 
            "user": username,
            "userid": userid,
            "data": str(self.su.get_user())
        })
