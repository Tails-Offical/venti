# -*- coding: UTF-8 -*-
import asyncio
import time
from tornado.web import authenticated
from project_demo.app_web.controller.controller_base import BaseHandler

class ControllerDemo2(BaseHandler):
    count1 = 0
    count2 = 0

    async def demo(self):
        ControllerDemo2.count1 += 1
        await asyncio.sleep(1)
        return (ControllerDemo2.count1, ControllerDemo2.count2)

    @authenticated
    async def post(self):
        s = time.time()
        ControllerDemo2.count2 += 1
        task = asyncio.create_task(self.demo())
        def callback(f):
            self.web_logger.info(f.result())
        task.add_done_callback(callback)
        self.web_logger.info(task.done())
        await task
        self.web_logger.info(task.done())
        results = await asyncio.gather(
            self.demo(),
            self.demo()
        )
        self.web_logger.info(str(results))
        f = time.time()
        self.write('cost: {:.2f}s'.format(f - s))
