# -*- coding: UTF-8 -*-
import json
from project_demo.app_web.controller.controller_base import BaseHandler

class LoginHandler(BaseHandler):
    async def post(self):
        request_data = json.loads(self.request.body)
        userid = request_data.get("userid")
        password = request_data.get("password")
        if userid == "tails@greypoints.com" and password == "123456":
            token = self.create_session(userid, 'tails')
            self.write({"msg": "success", "token": token})
        else:
            self.write({"msg": "error"})
