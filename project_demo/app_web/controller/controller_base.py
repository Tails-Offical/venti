# -*- coding: UTF-8 -*-
import time
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

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "http://localhost:9750")
        self.set_header("Access-Control-Allow-Headers", "Content-Type, Authorization")
        self.set_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS, PUT, DELETE")
        self.set_header("Access-Control-Allow-Credentials", "true")

    def options(self):
        self.set_status(204)
        self.finish()

    def remove_current_user(self):
        session_id = self.get_secure_cookie('session_id')
        if session_id:
            session_id = session_id.decode('utf-8')
            sessions.pop(session_id, None)
        self.clear_cookie('session_id')

    def get_current_user(self):
        session_id = self.get_secure_cookie('session_id')
        if session_id:
            session_id = session_id.decode('utf-8')
            session_data = sessions.get(session_id)
            if session_data:
                if session_data.get('expires_time', 0) > time.time():
                    formatted = session_data.copy()
                    formatted['login_time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(session_data['login_time']))
                    formatted['expires_time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(session_data['expires_time']))
                    return formatted
                else:
                    sessions.pop(session_id, None)
        return None
