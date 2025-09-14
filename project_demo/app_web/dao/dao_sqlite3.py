# -*- coding: UTF-8 -*-
import sqlite3

class DaoSqlite3:
    def __init__(self):
        self.conn = sqlite3.connect(':memory:')
        self.conn.row_factory = sqlite3.Row

    def get_user(self):
        self.conn.execute('''CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
        )''')
        self.conn.execute("INSERT INTO user (name) VALUES ('venti')")
        self.conn.execute("INSERT INTO user (name) VALUES ('tails')")
        self.conn.commit()
        cursor = self.conn.execute('SELECT * FROM user')
        return [dict(row) for row in cursor]