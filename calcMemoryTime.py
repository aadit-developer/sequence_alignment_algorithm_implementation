import time
import tracemalloc

def run(func, *args):
    tracemalloc.start()
    start = time.time()
    func(*args)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return time.time()-start, peak/10**6

# def x(a,b=10,c=20):
#     print(a,b,c)
#     ans = []
#     for i in range(100):
#         for j in range(30):
#             for k in range(100):
#                 ans.append((a,b,c))
#     return ans
#

# if __name__ == '__main__':
#     print(run(x, 5,4,3))