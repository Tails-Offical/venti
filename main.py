from venti.utils.vinject import Vinject
from venti.utils.vsys import ProcessHandler
# task1
from venti.controller.web_controller import make_app
from tornado.ioloop import IOLoop
# task2
from venti.controller.web_controller import HelloWebController

ij = Vinject()
yml_inject = ij.yml_get("web_inject.yml")

def task1():
    app = make_app(yml_inject)
    app.listen(2333)
    IOLoop.current().start()

def task2():
    oj = HelloWebController(yml_inject)
    print(oj.hello())

if __name__ == "__main__":
    handler = ProcessHandler(2)
    tasks = [task1, task2]
    handler.run(tasks)
