def sql_ijcheck(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, str) and ';' in arg:
                raise ValueError("Possible SQL injection detected: ';' in string argument!")
        for kwarg in kwargs.values():
            if isinstance(kwarg, str) and ';' in kwarg:
                raise ValueError("Possible SQL injection detected: ';' in string argument!")
        result = func(*args, **kwargs)
        return result
    return wrapper