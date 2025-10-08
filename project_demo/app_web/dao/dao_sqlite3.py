# -*- coding: UTF-8 -*-
import sqlite3

class DaoSqlite3:
    def __init__(self):
        self.conn = sqlite3.connect(':memory:')
        self.conn.row_factory = sqlite3.Row

    def get_user(self):
        self.conn.execute('''CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
        )''')
        self.conn.execute("INSERT INTO users (name) VALUES ('venti')")
        self.conn.commit()
        cursor = self.conn.execute('SELECT * FROM users')
        return [dict(row) for row in cursor]
