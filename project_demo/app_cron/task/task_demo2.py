# -*- coding: UTF-8 -*-

class TaskDemo2:
    async def step1(self, app_cron_logger):
        app_cron_logger.info('hello3')

    async def step2(self, app_cron_logger):
        app_cron_logger.info('hello4')

    async def exe(self, app_cron_logger):
        await self.step1(app_cron_logger)
        await self.step2(app_cron_logger)
