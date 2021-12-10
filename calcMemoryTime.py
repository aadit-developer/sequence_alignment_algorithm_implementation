import time
import tracemalloc


def run(func, *args):
    start = time.time()
    tracemalloc.start()
    res = func(*args)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return time.time() - start, peak / 1024, res
