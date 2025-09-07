# -*- coding: UTF-8 -*-
from loguru import logger

class Vlog:
    _handlers = {}

    def set_logger(path):
        if path not in Vlog._handlers:
            handler_id = logger.add(
                path,
                encoding="utf-8",
                enqueue=True,
                level="INFO"
            )
            Vlog._handlers[path] = handler_id
        return logger