"""List comprehension to replace map and filter."""

def main():
    a = [x for x in range(1, 11)]
    print(a)

    squares  = [x ** 2 for x in a]
    print(squares)

    even_squares = [x ** 2 for x in a if x % 2 == 0]
    print(even_squares)

    chile_ranks = {'ghost': 1, 'habanero':2, 'catenne': 3}
    rank_dict = {rank: name for name, rank in chile_ranks.items()}
    chile_len_set = {len(name) for name in rank_dict.values()}
    print(rank_dict)
    print(chile_len_set)

    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flat = [x for row in matrix for x in row]
    print(flat)
    
    b = [x for x in a if x > 4 if x % 2 == 0]
    c = [x for x in a if x > 4 and x % 2 == 0]
    print(b == c, b, c)

    value = [len(x) for x in open('./my_file.txt')]
    print(value)  # If file is huge, not to use it.

    it = (len(x) for x in open('./my_file.txt'))
    print(next(it))
    roots = ((x, x ** 0.5) for x in it)
    print(next(roots))


if __name__ == '__main__':
    main()
    