from loguru import logger

class Vlog:
    def __init__(self):
        self.logger = logger

    def set_logger(self, path):
        self.logger.add(
            path,
            encoding="utf-8",
            enqueue=True,
            level="INFO"
        )
        return self.logger
