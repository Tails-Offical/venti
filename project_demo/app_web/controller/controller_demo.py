# -*- coding: UTF-8 -*-
import asyncio
from project_demo.app_web.controller.controller_base import BaseHandler

class DemoHandler(BaseHandler):
    count1 = 0
    count2 = 0

    async def demo(self):
        DemoHandler.count1 += 1
        await asyncio.sleep(1)
        return DemoHandler.count1

    async def post(self):
        DemoHandler.count2 += 1
        task = asyncio.create_task(self.demo())
        def callback(f):
            self.web_logger.info(f.result())
        task.add_done_callback(callback)
        self.web_logger.info(task.done())
        await task
        self.web_logger.info(task.done())
        results = await asyncio.gather(
            self.demo(),
            self.demo(),
            self.demo()
        )
        self.web_logger.info(str(results))
        self.write('done')