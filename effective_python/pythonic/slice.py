"""Slice data."""

def main():
    """Main func."""
    a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    print('First four: ', a[:4])
    print('Last four: ', a[-4:])
    print('Middle two: ', a[3:-3])

    a[len(a):] = ['i']
    print(a)

    odds = a[::2]
    print(odds)
    evens = a[1::2]
    print(evens)
    evens = a[::-2]
    print(evens)
    print(a[2::2])

    x = b'2017'
    x = x[::-1]
    print(x)

if __name__ == '__main__':
    main()
    