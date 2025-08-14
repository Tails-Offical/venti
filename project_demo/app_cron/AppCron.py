# -*- coding: UTF-8 -*-
import os
import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from venti.vlog import Vlog
from project_demo.app_cron.task.task_demo1 import TaskDemo1
from project_demo.app_cron.task.task_demo2 import TaskDemo2

class AppCron:
    def __init__(self, venti_queue, venti_dict, venti_event, venti_lock, path, stype):
        self.venti_queue = venti_queue
        self.venti_dict = venti_dict
        self.venti_event = venti_event
        self.venti_lock = venti_lock
        self.path = path
        self.stype = stype
        self.vlog = Vlog()
        self.app_cron_logger = self.vlog.set_logger(os.path.join(self.path, 'data','project_demo','log','app_cron.log'))

    async def task1(self):
        await TaskDemo1().exe(self.app_cron_logger)

    async def task2(self):
        await TaskDemo2().exe(self.app_cron_logger)

    async def _scheduler(self):
        scheduler = AsyncIOScheduler()
        scheduler.add_job(self.task1, "interval", seconds=3)
        scheduler.add_job(self.task2, "cron", hour=22, minute=1)
        scheduler.start()
        try:
            await asyncio.to_thread(self.venti_event.wait)
        finally:
            scheduler.shutdown()

    def cron(self):
        self.app_cron_logger.info('app_cron start')
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self._scheduler())
        self.app_cron_logger.info('app_cron fin')

