"""Closure."""
from assertpy import assert_that

def sort_priority(values, group):
    def helper(x):
        if x in group:
            return (0, x)
        return(1 ,x)
    values.sort(key=helper)

def sort_priority2(numbers, group):
    found = False
    def helper(x):
        if x in group:
            found = True  # Bug
            return(0, x)
        return(1, x)
    numbers.sort(key=helper)
    return found

def sort_priority3(numbers, group):
    found = False
    def helper(x):
        nonlocal found
        if x in group:
            found = True
            return(0, x)
        return(1, x)
    numbers.sort(key=helper)
    return found

class Sorter(object):
    def __init__(self, group):
        self.group = group
        self.found = False

    def __call__(self, x):
        if x in self.group:
            self.found = True
            return(0, x)
        return(1, x)
    

def main():
    numbers = [8, 7, 3, 4, 5, 2, 1]
    group = {8, 7, 4}
    sort_priority(numbers, group)
    print(numbers)
    sort_priority2(numbers, group)
    print(numbers)

    sorter = Sorter(group)
    numbers.sort(key=sorter)
    assert_that(sorter.found).is_true()
    print(numbers)

if __name__ == '__main__':
    main()
    