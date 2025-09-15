# -*- coding: UTF-8 -*-
from project_demo.app_web.dao.dao_sqlite3 import DaoSqlite3
from project_demo.app_web.dao.dao_users import DaoUsers

class ServiceUser:
    def __init__(self):
        self.dq = DaoSqlite3()

    def get_user(self):
        return self.dq.get_user()
    
    def get_user2(self):
        du = DaoUsers()
        du.create_table()
        du.add_user()
        return [du.get_user_by_id("1"), du.get_user_by_id2("1")]
