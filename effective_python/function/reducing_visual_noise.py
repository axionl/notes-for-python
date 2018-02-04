"""Reducing visual_noise."""

def log(message, *values):
    if not values:
        print(message)
    else:
        values_str = ','.join(str(x) for x in values)
        print('%s: %s' % (message, values_str))

def log2(sequence, message, *values):
    if not values:
        print('%s: %s' % (sequence, message))
    else:
        values_str = ', '.join(str(x) for x in values)
        print('%s: %s: %s' % (sequence, message, values_str))

def my_generator():
    for i in range(10):
        yield i

def my_func(*args):
    print(args)

def main():
    log('My numbers are', [1, 2])
    log('Hi there')

    favorites = [7, 33, 99]
    log('Favorite colors', *favorites)

    it = my_generator()
    my_func(*it)

    log2(1, 'Favorites', 7 ,33)


if __name__ == '__main__':
    main()
