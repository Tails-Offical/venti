# -*- coding: UTF-8 -*-
import json
import uuid
import time
from project_demo.app_web.controller.controller_base import BaseHandler, sessions

class ControllerLogin(BaseHandler):
    async def post(self):
        try:
            request_data = json.loads(self.request.body)
            account = request_data.get("account")
            password = request_data.get("password")
            if account == 'demo@greypoints.com' and password == '123456':
                session_id = str(uuid.uuid4())
                session_data = {
                    'account': account.strip(),
                    'login_time': time.time(),
                    'expires_time': time.time() + 60*60*24,
                    'ip': self.request.remote_ip,
                    'user_agent': self.request.headers.get('User-Agent', '')
                }
                sessions[session_id] = session_data
                self.set_secure_cookie('session_id', session_id, httponly=True, expires_days=1)
                self.set_status(200)
                self.write({"msg":"success"})
            else:
                self.set_status(401)
                self.write({"msg": 'account or password error'})
        except Exception as e:
            self.set_status(500)
            self.write({"msg": "{}".format(e)})
