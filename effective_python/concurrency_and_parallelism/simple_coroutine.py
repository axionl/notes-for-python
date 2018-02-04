def my_coroutine():
    while True:
        received = yield
        print("Received:", received)

def minimize():
    current = yield
    while True:
        value = yield current
        current = min(value, current)

def main():
    it = my_coroutine()
    next(it)
    it.send("First")
    it.send("Second")

    it = minimize()
    next(it)
    print(it.send(10))
    print(it.send(4))
    print(it.send(22))
    print(it.send(-1))


if __name__ == '__main__':
    main()
