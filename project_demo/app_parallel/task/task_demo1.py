# -*- coding: UTF-8 -*-

class TaskDemo1:
    def __init__(self, concurrent_logger):
        self.concurrent_logger = concurrent_logger

    def task(self):
        self.concurrent_logger.info('parallel TaskDemo1')