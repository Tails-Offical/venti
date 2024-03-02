import psutil
import sys
import multiprocessing
import concurrent.futures

class SysInfo:
    def sys_type(self):
        st = sys.platform
        return st

    def hardware(self):
        if 'win' in self.sys_type() or 'linux' in self.sys_type():
            logicCore = psutil.cpu_count(logical=True)
            memSize = round(psutil.virtual_memory().total/1024**3)
            hardware = {"LogicCore":logicCore,"MemSize_G":memSize}
            return hardware
        else:
            return "Unsupported Sys"

class ProcessHandler:
    def __init__(self, worker_count):
        self.worker_count = worker_count
        self.pool = multiprocessing.Pool(worker_count)
        self.manager = multiprocessing.Manager()
        self.queue = self.manager.Queue()
        self.lock = self.manager.Lock()

    def run(self, tasks):
        for task in tasks:
            self.pool.apply_async(task)
        self.pool.close()
        self.pool.join()

    def run_arg(self, task, args_list):
        for args in args_list:
            self.pool.apply_async(task, args=(self.queue, self.lock,) + args)
        self.pool.close()
        self.pool.join()

    def get_results(self):
        results = []
        while not self.queue.empty():
            results.append(self.queue.get())
        return results

class ThreadHandler:
    def __init__(self, max_workers):
        self.max_workers = max_workers
        self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=max_workers)
        self.futures = []

    def run(self, tasks):
        for task in tasks:
            future = self.executor.submit(task)
            self.futures.append(future)

    def run_arg(self, task, args_list):
        for args in args_list:
            future = self.executor.submit(task, *args)
            self.futures.append(future)

    def get_results(self):
        results = []
        for future in concurrent.futures.as_completed(self.futures):
            try:
                result = future.result()
                results.append(result)
            except Exception as e:
                print(f"A task raised an exception: {e}")
        return results

    def shutdown(self):
        self.executor.shutdown()
