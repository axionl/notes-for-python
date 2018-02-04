from threading import Lock
from contextlib import contextmanager
import logging

lock = Lock()

def test1():
    lock.acquire()
    try:
        print('Lock is held')
    finally:
        lock.release()

def test2():
    """With is better than try-finally."""
    with lock:
        print('Lock is held')

def my_function():
    logging.debug('Some debug data')
    logging.error('Error log here')
    logging.debug('More debug data')

@contextmanager
def debug_logging(level):
    logger = logging.getLogger()
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield
    finally:
        logger.setLevel(old_level)

@contextmanager
def log_level(level, name):
    logger = logging.getLogger(name)
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield logger
    finally:
        logger.setLevel(old_level)

def main():
    with debug_logging(logging.DEBUG):
        print('Inside')
        my_function()
    print('After:')
    my_function()

    with log_level(logging.DEBUG, 'my-log') as logger:
        logger.debug('This is my message')
        logging.debug('Thins will not print')

if __name__ == '__main__':
    main()
    