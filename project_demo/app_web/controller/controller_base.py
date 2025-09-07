# -*- coding: UTF-8 -*-
import time
import uuid
from tornado.web import RequestHandler

sessions = {}

class BaseHandler(RequestHandler):
    def initialize(self, osname, path, venti_plock, venti_pevent, venti_pqueue, venti_pdict, web_logger):
        self.osname = osname
        self.path = path
        self.venti_plock = venti_plock
        self.venti_pevent = venti_pevent
        self.venti_pqueue = venti_pqueue
        self.venti_pdict = venti_pdict
        self.web_logger = web_logger

    def get_current_user(self):
        token = self.get_secure_cookie("token")
        if token:
            token = token.decode('utf-8')
            session_data = sessions.get(token)
            if session_data:
                if time.time() - session_data.get("time", 0) > 60:
                    del sessions[token]
                    return None
                # active time
                session_data["time"] = time.time()
                return session_data
        return None

    def create_session(self, userid, username):
        token = str(uuid.uuid4())
        sessions[token] = {
            "userid": userid,
            "name": username,
            "time": time.time()
        }
        self.set_secure_cookie("token", token)
        return token

    def remove_session(self):
        token = self.get_secure_cookie("token")
        if token:
            token = token.decode('utf-8')
            if token in sessions:
                del sessions[token]
        self.clear_cookie("token")
        return True
