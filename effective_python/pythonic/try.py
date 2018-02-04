"""Try to test error."""
import json


def divide_json(path):
    UNDEFIND = object()
    handle = open(path, 'r+')
    try:
        data = handle.read()
        op = json.loads(data)
        value = (
            op['numerator'] /
            op['denominator'])
    except ZeroDivisionError as e:
        return UNDEFIND
    else:
        op['result'] = value
        result = json.dumps(op)
        handle.seek(0)
        handle.write(result)
        return value
    finally:
        handle.close()

def main():
    path = './test.txt'
    f = divide_json(path)

if __name__ == '__main__':
    main()
    
