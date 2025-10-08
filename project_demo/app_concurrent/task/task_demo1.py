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
            await client.post(
                "http://localhost:9750/login", 
                json={
                "account": "demo@greypoints.com",
                "password": "123456"
                },
                headers={"Content-Type": "application/json"}
            )          
            s = time.time()
            for _ in range(2):
                task.append((self.fetch(client, "http://localhost:9750/demo2")))
            await asyncio.gather(*task)
            # for c in asyncio.as_completed(task):
            #     print(c)
            f = time.time()
            await client.post("http://localhost:9750/logout")
        self.concurrent_logger.info('cost: {:.2f}s'.format(f - s))
