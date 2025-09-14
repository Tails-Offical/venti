# -*- coding: UTF-8 -*-
from project_demo.app_web.dao.dao_sqlite3 import DaoSqlite3

class ServiceUser:
    def __init__(self):
        self.dq = DaoSqlite3()

    def get_user(self):
        return self.dq.get_user()
