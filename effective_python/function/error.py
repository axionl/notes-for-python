"""Error."""

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError('Invalid inputs') from e

def main():
    """Main func."""
    x, y = 5, 0
    try:
        result = divide(x, y)
    except ValueError:
        print('Invalid inputs.')
    else:
        print('Result is %.1f' % result)

if __name__ == '__main__':
    main()
    