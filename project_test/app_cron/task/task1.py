# -*- coding: UTF-8 -*-

class Task1(object):
    async def step1(self):
        print('hello1')

    async def step2(self):
        print('hello12')
        raise Exception('hello1233')

    async def exe(self):
        await self.step1()
        await self.step2()
