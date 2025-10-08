# -*- coding: UTF-8 -*-
import os
import aiofiles
from project_demo.app_web.controller.controller_base import BaseHandler

class ControllerDownload(BaseHandler):
    async def get(self):
        try:
            filename = self.get_query_argument('filename')
            upload_dir = os.path.join(self.path, 'data', 'project_demo', 'upload')
            file_path = os.path.join(upload_dir, os.path.basename(filename))
            self.set_header('Content-Type', 'application/octet-stream')
            self.set_header('Content-Disposition', f'attachment; filename="{os.path.basename(file_path)}"')
            self.set_header('Content-Length', str(os.path.getsize(file_path)))
            chunk_size = 1 * 1024 ** 2
            async with aiofiles.open(file_path, 'rb') as f:
                while True:
                    chunk = await f.read(chunk_size)
                    if not chunk:
                        break
                    self.write(chunk)
                    await self.flush()
        except Exception as e:
            self.set_status(500)
            self.write({"error": "{}".format(str(e))})
        return
