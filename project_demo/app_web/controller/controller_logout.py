# -*- coding: UTF-8 -*-
from project_demo.app_web.controller.controller_base import BaseHandler

class Logout(BaseHandler):
    async def post(self):
        self.remove_session()
        self.write({"msg": "logged out"})
