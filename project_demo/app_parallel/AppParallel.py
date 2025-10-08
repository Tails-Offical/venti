# -*- coding: UTF-8 -*-
import os
from multiprocessing import Process
from venti.vlog import Vlog
from project_demo.app_parallel.task.task_demo1 import TaskDemo1
from project_demo.app_parallel.task.task_demo2 import TaskDemo2

class AppParallel:
    def __init__(self, osname, path, venti_plock, venti_pevent, venti_pqueue, venti_pdict):
        self.osname = osname
        self.path = path
        self.venti_plock = venti_plock
        self.venti_pevent = venti_pevent
        self.venti_pqueue = venti_pqueue
        self.venti_pdict = venti_pdict

    def task_demo1(self):
        app_parallel_logger = Vlog.set_logger(os.path.join(self.path, 'data','project_demo','log','app_parallel.log'))
        pid = os.getpid()
        app_parallel_logger.info(f"task_demo1 {pid}")
        TaskDemo1(app_parallel_logger).task()

    def task_demo2(self):
        app_parallel_logger = Vlog.set_logger(os.path.join(self.path, 'data','project_demo','log','app_parallel.log'))
        pid = os.getpid()
        app_parallel_logger.info(f"task_demo2 {pid}")
        TaskDemo2(app_parallel_logger).task()

    @staticmethod
    def app(osname, path, processes, venti_plock, venti_pevent, venti_pqueue, venti_pdict):
        ap = AppParallel(osname, path, venti_plock, venti_pevent, venti_pqueue, venti_pdict)
        processes.append(Process(target=ap.task_demo1))
        processes.append(Process(target=ap.task_demo2))
