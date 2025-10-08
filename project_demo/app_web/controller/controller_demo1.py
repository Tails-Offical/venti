# -*- coding: UTF-8 -*-
from project_demo.app_web.controller.controller_base import BaseHandler
from project_demo.app_web.service.service_user import ServiceUser

class ControllerDemo1(BaseHandler):
    async def post(self):
        current_user = self.get_current_user()
        if current_user:
            self.set_status(200)
            self.finish({
                "msg": "success",
                "result": "{}".format(ServiceUser().get_user())
            })
        else:
            self.set_status(401)
            self.finish({"msg": "unauthorized"})
