import time
from memory_profiler import memory_usage
from multiprocessing import freeze_support


def run(func, *args):
    freeze_support()
    start = time.time()
    mem_usage = memory_usage((func, args), interval=0.2)
    print(max(mem_usage))
    return (time.time()-start), max(mem_usage)


# def x(a,b=10,c=20):
#     print(a,b,c)
#     ans = []
#     for i in range(10000):
#         for j in range(30):
#             for k in range(100):
#                 ans.append((a,b,c))
#     return ans
#
#
# if __name__ == '__main__':
#     print(run(x, 5,4,3))