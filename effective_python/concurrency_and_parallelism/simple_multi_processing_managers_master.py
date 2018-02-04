import random
import time
import queue

from multiprocessing.managers import BaseManager


class QueueManager(BaseManager):
    pass


def main():
    task_queue = queue.Queue()
    result_queue = queue.Queue()

    QueueManager.register('get_task_queue', callable=lambda: task_queue)
    QueueManager.register('get_result_queue', callable=lambda: result_queue)

    manager = QueueManager(address=('localhost', 5000), authkey=b'5fvsd49ijnz37p')
    manager.start()

    task = manager.get_task_queue()
    result = manager.get_result_queue()

    for i in range(10):
        num = random.randint(0, 10000)
        print('Put task %d' % num)
        task.put(num)

    print('Try get result...')
    for i in range(10):
        results = result.get(timeout=10)
        print('Result: %s' % results)

    manager.shutdown()
    print('Exit')

if __name__ == '__main__':
    main()
