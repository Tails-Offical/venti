# -*- coding: UTF-8 -*-

class TaskDemo1:
    async def step1(self, app_cron_logger):
        app_cron_logger.info('hello1')

    async def step2(self, app_cron_logger):
        app_cron_logger.info('hello2')

    async def exe(self, app_cron_logger):
        await self.step1(app_cron_logger)
        await self.step2(app_cron_logger)
