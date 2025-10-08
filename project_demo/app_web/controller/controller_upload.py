# -*- coding: UTF-8 -*-
import os
import uuid
import asyncio
from tornado.web import stream_request_body
from project_demo.app_web.controller.controller_base import BaseHandler

@stream_request_body
class ControllerUpload(BaseHandler):
    async def prepare(self):
        self.chunk_size = 1 * 1024 ** 2
        upload_dir = os.path.join(self.path, 'data', 'project_demo', 'upload')
        os.makedirs(upload_dir, exist_ok=True)
        filename = self.request.headers.get('X-Filename') or self.get_query_argument('filename', None)
        if filename:
            safe_name = os.path.basename(filename)
        else:
            safe_name = str(uuid.uuid4())
        self._file_path = os.path.join(upload_dir, safe_name)
        self._f = open(self._file_path, 'wb')
        self._loop = asyncio.get_running_loop()
        self._pending = []

    def data_received(self, chunk):
        if not chunk:
            return
        fut = self._loop.run_in_executor(None, self._f.write, chunk)
        self._pending.append(fut)

    async def post(self):
        try:
            if self._pending:
                await asyncio.gather(*self._pending)
            self._f.flush()
        except Exception as e:
            print(e)
        finally:
            self._f.close()
