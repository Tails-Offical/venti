# -*- coding: UTF-8 -*-

class Task2(object):
    async def step1(self):
        print('hello3')

    async def step2(self):
        print('hello4')

    async def exe(self):
        await self.step1()
        await self.step2()
