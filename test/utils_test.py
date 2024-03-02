import base

# ------ ------ --- valgo --- ------ ------
from venti.utils.valgo import *

def ut1():
    ms = MergeSorter()
    data = [3, 6, 1, 5, 8, 2, 9, 7, 4]
    sorted_list = ms.sort(data)
    print(sorted_list)

# ------ ------ --- vdata --- ------ ------
from venti.utils.vdata import *

def ut2():
    ah = AccuracyHandler()
    print(ah.half_adjust("3.14159265", 2))

def ut3():
    th = TimeHandler
    ts = th.timestamp()
    print(ts)
    print(th.timestamp_to_datetime(ts))
    t1 = th.timestamp("2023-09-25 00:00")
    t2 = th.timestamp("2023-09-26 12:00")
    difference_in_seconds = th.time_difference(t1, t2)  
    print(difference_in_seconds)
    print(th.get_time())
    print(th.get_date())

def ut4():
    fh = FileHandler
    ftb = fh.file_to_binary("resource/temp/hello.venti",3)
    fh.binary_to_file(ftb,"resource/temp/venti.hello")
    print(fh.check_encoding('resource/temp/hello.txt'))
    fh.change_encoding('resource/temp/hello.txt','gbk')
    print(fh.check_encoding('resource/temp/hello.txt_gbk'))
    print(fh.file_hash('resource/temp/hello.txt_gbk'))
    # fh.compress("resource/temp","233.tar.xz")
    # fh.decompression("233.tar.xz",".")

def ut5():
    sh = StrHandler
    print(sh.str_hash("Hello Venti!"))
    en = sh.str_encryption("Hello Venti!")
    print(en)
    print(sh.str_decrypt(en['str'], en['key']))
    stb = sh.str_to_binary("Venti")
    print(stb)
    print(sh.binary_to_str(stb))

def ut6():
    ch = CodeHandler
    ch.qrcode_character("Hello Venti !")

def ut7():
    yh = YmlHandler
    # yh.yml_write()
    print(yh.yml_load("venti/config/inject/web_inject.yml"))

class ut8(MariaHandler):
    pass
db_handler = ut8(ac='root',
                pw='GreyPoints',
                host='localhost',
                port=3306,
                db='test')
'''
query = 'SHOW TABLES'
tables = db_handler.exe(query)
for table in tables:
    print(table)
'''
'''
queries = [
    "SELECT * FROM t1 WHERE id = %s",
    "SELECT * FROM t1 WHERE name = %s"
]
args = [(1), ('tails2')]
rs=db_handler.transaction(queries,args)
print(rs)
'''

class ut9(RedisHandler):
    pass
'''
rh = ut9(host='localhost',
        port=6379,
        db=0,
        password='GreyPoints')
rh.hash_set("hash_test1", "k1", "v1")
print(rh.hash_get("hash_test1", "k1"))
commands = [
    ("hset", "hash_test1", "k2", "v2"),
    ("hset", "hash_test1", "k3", "v3")
]
rh.transaction(commands)
'''

# ------ ------ --- vnet --- ------ ------
from venti.utils.vnet import *
from tornado.web import Application
from tornado.ioloop import IOLoop, PeriodicCallback

class ut10(AsyncHandler):
    async def get(self):
        await super().get()
        handler = AsyncClientHandler()
        result = await handler.get(url='https://httpbin.org/get')
        self.write(str(result))
'''
def make_app():
    return Application([
        (r"/", ut10),
    ])
app = make_app()
app.listen(8888)
IOLoop.current().start()
'''
class ut11(AsyncClientHandler):
    pass
'''
ach = ut11()
loop = IOLoop.current()
async def AsyncPost():
    result = await ach.post(url='https://httpbin.org/post',body={'name':'venti'})
    print(str(result))
    loop.stop()
loop.add_callback(AsyncPost)
loop.start()
'''
# ------ ------ --- vsys --- ------ ------
from venti.utils.vsys import *
import threading
import time
def ut12():
    si = SysInfo()
    print(si.sys_type())
    print(si.hardware())

def ut13():
    print(os.getpid())
"""
if __name__ == '__main__':
    ph = ProcessHandler(2)
    tasks = [ut13 for _ in range(12)]
    ph.run(tasks)
"""

class ut14(ThreadHandler):
    def ttask(self):
        print(threading.current_thread().ident)
        time.sleep(2)
# th = ut14(2)
# tasks = [th.ttask for _ in range(12)]
# th.run(tasks)
# th.shutdown()

