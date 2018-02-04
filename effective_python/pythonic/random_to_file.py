"""Create a random file."""

import os
import time

def main():
    """Main func."""
    path = './random.bin'
    with open(path, 'wb') as f:
        f.write(os.urandom(10))
    time.sleep(3)
    try:
        os.remove(path)
    except FileNotFoundError:
        pass

if __name__ == '__main__':
    main()      
