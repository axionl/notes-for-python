from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from multiprocessing import cpu_count
from time import time


def gcd(pair):
    a, b = pair
    low = min(a, b)
    for i in range(low, 0, -1):
        if a % i == 0 and b % i == 0:
            return i
    
def main():
    numbers = [(1963309, 2265973), (2030677, 3814172),
        (1551645, 2229620), (2039045, 2020802)]
    start = time()
    result = list(map(gcd, numbers))
    end = time()
    print('Took %.3f seconds' % (end - start))

    start = time()
    pool = ThreadPoolExecutor(max_workers=cpu_count())
    result = list(pool.map(gcd, numbers))
    end = time()
    print('Took %.3f seconds' % (end - start))

    start = time()
    pool = ProcessPoolExecutor(max_workers=cpu_count())
    result = list(pool.map(gcd, numbers))
    end = time()
    print('Took %.3f seconds' % (end - start))

if __name__ == '__main__':
    main()