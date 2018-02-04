from profile import Profile
from pstats import Stats
from random import randint


def insertion_sort(data):
    result = []
    for value in data:
        insert_value(result, value)
    return result

def insert_value(array, value):
    for i, existing in enumerate(array):
        if existing > value:
            array.insert(i, value)
            return
    array.append(value)

def main():
    max_size = 10 ** 4
    data = [randint(0, max_size) for _ in range(max_size)]
    test = lambda: insertion_sort(data)

    profiler = Profile()
    profiler.runcall(test)

    stats = Stats(profiler)
    stats.strip_dirs()
    stats.sort_stats('cumulative')
    stats.print_stats()
    stats.print_callers()

if __name__ == '__main__':
    main()
