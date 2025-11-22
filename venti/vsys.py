# -*- coding: UTF-8 -*-
import sys
from functools import wraps

class Vsys:
    @staticmethod
    def stdout_file(file_path):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                original_stdout = sys.stdout
                try:
                    with open(file_path, "w", encoding="utf-8") as f:
                        sys.stdout = f
                        result = func(*args, **kwargs)
                finally:
                    sys.stdout = original_stdout
                return result
            return wrapper
        return decorator