"""Parse."""

from urllib.parse import parse_qs


def get_first_int(values, key, default=0):
    """Packing to func."""
    found = values.get(key, [''])
    if found[0]:
        found = int(found[0])
    else:
        found = default
    return found

def main():
    """Main func."""
    my_values = parse_qs('red=5&blue=0&green=', keep_blank_values=True)

    print(repr(my_values))
    print('Red: ', my_values.get('red'))
    print('Blue: ', my_values.get('blue'))
    print('Green: ', my_values.get('green'))
    print('Opacity: ', my_values.get('opacity'))

    red = my_values.get('red')[0] or 0
    print(red)

    opacity = my_values.get('opacity', [''])[0] or 0
    print(opacity)

    green = my_values.get('green', [''])
    if green[0]:
        green = int(green[0])
    else:
        green = 0
    print(green)

    green = get_first_int(my_values, 'green')
    print(green)


if __name__ == '__main__':
    main()
    
