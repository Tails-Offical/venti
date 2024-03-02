import time

def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        time_diff = end_time - start_time
        # print(f"{func.__name__} ran in {time_diff} seconds.")
        return result, str(time_diff)+' s'
    return wrapper
