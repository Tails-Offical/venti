# -*- coding: UTF-8 -*-
from project_demo.app_web.controller.controller_base import BaseHandler

class ControllerLogout(BaseHandler):
    async def post(self):
        self.remove_current_user()
        self.write({"msg": "logout"})
