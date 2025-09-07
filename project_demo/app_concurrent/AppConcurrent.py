# -*- coding: UTF-8 -*-
import os
import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from multiprocessing import Process
from venti.vlog import Vlog
from project_demo.app_concurrent.task.task_demo1 import TaskDemo1
from project_demo.app_concurrent.task.task_demo2 import TaskDemo2

class AppConcurrent:
    def __init__(self, osname, path, venti_plock, venti_pevent, venti_pqueue, venti_pdict):
        self.osname = osname
        self.path = path
        self.venti_plock = venti_plock
        self.venti_pevent = venti_pevent
        self.venti_pqueue = venti_pqueue
        self.venti_pdict = venti_pdict

    async def task1_job(self, concurrent_logger):
        await TaskDemo1(concurrent_logger).task()

    async def task2_job(self, concurrent_logger):
        await TaskDemo2(concurrent_logger).task()

    async def run_scheduler(self):
        concurrent_logger = Vlog.set_logger(os.path.join(self.path, 'data','project_demo','log','app_concurrent.log'))
        scheduler = AsyncIOScheduler()
        scheduler.add_job(self.task1_job, "interval", seconds=10, args=[concurrent_logger])
        scheduler.add_job(self.task2_job, "cron", hour=22, minute=1, args=[concurrent_logger])
        scheduler.start()
        try:
            await asyncio.to_thread(self.venti_pevent.wait)
        finally:
            scheduler.shutdown()

    def loop(self):
        asyncio.run(self.run_scheduler())

    @staticmethod
    def app(osname, path, processes, venti_plock, venti_pevent, venti_pqueue, venti_pdict):
        ac = AppConcurrent(osname, path, venti_plock, venti_pevent, venti_pqueue, venti_pdict)
        processes.append(Process(target=ac.loop))
