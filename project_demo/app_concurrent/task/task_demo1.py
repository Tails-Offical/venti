# -*- coding: UTF-8 -*-
import asyncio
import httpx
import time

class TaskDemo1:
    def __init__(self, concurrent_logger):
        self.concurrent_logger = concurrent_logger

    async def fetch(self, client, url):
        response = await client.post(url)
        self.concurrent_logger.info(f"{response.text}")

    async def task(self):
        task = []
        async with httpx.AsyncClient() as client:
            start = time.time()
            for _ in range(2):
                task.append((self.fetch(client, "http://localhost:9750/demo")))
            await asyncio.gather(*task)
            fin = time.time()
        self.concurrent_logger.info('concurrent TaskDemo1 {}'.format(fin-start))
