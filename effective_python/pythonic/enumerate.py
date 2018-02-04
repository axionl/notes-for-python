"""Use enumerate instead of range."""

from random import randint


def main():
    """Main func."""
    random_bits = 0
    for i in range(64):
        if randint(0, 1):
            random_bits |= 1 << i
            print(random_bits)

    flavor_list = ['vanilla', 'chocolate', 'pecan', 'strawberry']
    for i in range(len(flavor_list)):
        print('%d: %s' % (i + 1, flavor_list[i]))

    for i, flavor in enumerate(flavor_list):
        print('%d: %s' % (i + 1, flavor))

if __name__ == '__main__':
    main()
