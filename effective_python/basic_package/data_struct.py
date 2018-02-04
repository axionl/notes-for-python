from bisect import bisect_left
from collections import OrderedDict, defaultdict, deque
from functools import wraps
from heapq import heappop, heappush, nsmallest
from random import randint
from time import time


def fn_timer(function):
    @wraps(function)
    def function_timer(*args, **kwargs):
        t0 = time()
        result = function(*args, **kwargs)
        t1 = time()
        print("Total time running: %s seconds" % (str(t1-t0)))
        return result
    return function_timer

def fifo():
    fifo = deque()
    for i in range(5):
        fifo.append(i)
    x = fifo.popleft()
    print(fifo, ':', x)

def fast_hash_table():
    a = {}
    a['foo'] = 1
    a['bar'] = 2

    b = {}
    b['bar'] = 2
    b['foo'] = 1
    print(a)
    print(b)
    print('Equal?', a == b)

    a = OrderedDict()
    a['foo'] = 1
    a['bar'] = 2

    b = OrderedDict()
    b['bar'] = 'red'
    b['foo'] = 'blue'
    for value1, value2 in zip(a.values(), b.values()):
        print(value1, value2)

def default_key_dict():
    stats = defaultdict(int)
    stats['my_counter'] += 1
    stats['empty'] # default value is 0
    print(stats)

def heap():
    a = []
    for i in range(5):
        heappush(a, i)
    print(a)

    assert a[0] == nsmallest(1, a)[0] == 0

    for i in range(5):
        print(heappop(a))
    print(a)


@fn_timer
def bisect_left_module_1():
    x = list(range(10 ** 7))
    i = x.index(9912342)
    print(i)

@fn_timer
def bisect_left_module_2():
    x = list(range(10 ** 7))
    i = bisect_left(x, 9912342)
    print(i)

def main():
    fifo()
    fast_hash_table()
    default_key_dict()
    heap()
    bisect_left_module_1()
    bisect_left_module_2()

if __name__ == '__main__':
    main()
