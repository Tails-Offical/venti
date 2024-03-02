from venti.repository.interfaces.web_repository_interface import WebRepositoryInterface
from venti.utils.vsys import SysInfo
from venti.utils.handler.timing_handler import timeit
import sqlite3

class HelloWebRepositoryImplement:
    @timeit
    def hello(self):
        return 'Hello WebRepositoryImplement'

class WebRepositoryImplement(WebRepositoryInterface):
    @timeit
    def _work(self, od):
        if 'win' in SysInfo().sys_type():
            con = sqlite3.connect('resource\\db\\demo.db')
        elif 'linux' in SysInfo().sys_type():
            con = sqlite3.connect('resource/db/demo.db')
        try:
            cursor = con.cursor()
            cursor.execute("BEGIN TRANSACTION;")
            cursor.execute(od)
            result = cursor.fetchall()
            cursor.execute("COMMIT;")
            return result
        except sqlite3.Error as e:
            con.execute("ROLLBACK;")
            return e
        except Exception as f:
            con.execute("ROLLBACK;")
            return f
        finally:
            con.close()

    def get_data(self):
        tg = 'SELECT DemoColumn FROM DemoTable;'
        exe = self._work(tg)
        return exe
