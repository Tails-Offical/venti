# -*- coding: UTF-8 -*-
from datetime import datetime, timezone
import time
from functools import wraps

class Vtime:
    @staticmethod
    def utc_get_time():
        gt = datetime.now(timezone.utc).strftime("%H:%M:%S")
        return gt
    @staticmethod
    def utc_get_date():  
        gt = datetime.now(timezone.utc).strftime("%Y-%m-%d")  
        return gt
    @staticmethod
    def utc_timestamp():
        return datetime.now(timezone.utc).timestamp()
    @staticmethod
    def utc_timestamp_to_datetime(ts):
        return datetime.fromtimestamp(ts, timezone.utc)

    @staticmethod
    def get_time():
        return datetime.now().strftime("%H:%M:%S")
    @staticmethod
    def get_date():
        return datetime.now().strftime("%Y-%m-%d")
    @staticmethod
    def timestamp():
        return datetime.now().timestamp()
    @staticmethod
    def timestamp_to_datetime(ts):
        return datetime.fromtimestamp(ts)

    @staticmethod
    def timeit(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"{func.__name__} executed {elapsed_time:.0f} seconds")
            return result
        return wrapper