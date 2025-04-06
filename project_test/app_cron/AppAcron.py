# -*- coding: UTF-8 -*-
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import asyncio
from project_test.app_cron.task.task1 import Task1
from project_test.app_cron.task.task2 import Task2
from functools import wraps

def exception_handler(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except Exception as e:
            print(f"Error in {func.__name__}: {e}")
    return wrapper

class AppAcron:
    def __init__(self, stop_event, logger, path):
        self.stop_event = stop_event
        self.scheduler = AsyncIOScheduler()
        self.logger = logger
        self.path = path

    @exception_handler
    async def task1(self):
        await Task1().exe()

    @exception_handler
    async def task2(self):
        await Task2().exe()

    async def exe(self):
        self.scheduler.add_job(self.task1, "interval", seconds=60)
        self.scheduler.add_job(self.task2, "cron", hour=17, minute=47)
        self.scheduler.start()
        while not self.stop_event.is_set():
            await asyncio.sleep(3)
        self.scheduler.shutdown()