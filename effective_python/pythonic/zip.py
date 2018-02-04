"""Using zip."""

def main():
    """Main func."""
    names = ['Cecilia', 'Lise', 'Marie']
    letters = [len(n) for n in names]
    print('letters: ', letters)

    longest_name = None
    max_letters = 0

    for i, name in enumerate(names):
        count = letters[i]
        if count > max_letters:
            longest_name = name
            max_letters = count

    print(longest_name, max_letters)

    for name, count in zip(names, letters):
        if count > max_letters:
            longest_name = name
            max_letters = count
    print(longest_name, max_letters)


if __name__ == '__main__':
    main()
