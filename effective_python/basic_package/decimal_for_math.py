from decimal import Decimal, ROUND_UP

def main():
    rate = 1.45
    seconds = 3 * 60 + 42
    cost = rate * seconds / 60
    print(cost)
    print(round(cost, 2))

    rate = Decimal('1.45')
    seconds = Decimal('%s' % (3 * 60 + 42))
    print(seconds)
    cost = rate * seconds / Decimal('60')
    print(cost, type(cost))
    rounded = cost.quantize(Decimal('0.01'), rounding=ROUND_UP)
    print(rounded)

if __name__ == '__main__':
    main()
