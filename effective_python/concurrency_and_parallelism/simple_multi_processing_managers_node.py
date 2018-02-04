import time
from queue import Queue
from multiprocessing.managers import BaseManager


class QueueManager(BaseManager):
    pass


def main():
    QueueManager.register('get_task_queue')
    QueueManager.register('get_result_queue')

    server_addr = 'localhost'
    print('Connecting to server %s...' % server_addr)

    manager = QueueManager(address=(server_addr, 5000), authkey=b'5fvsd49ijnz37p')
    manager.connect()

    task = manager.get_task_queue()
    result = manager.get_result_queue()

    for i in range(10):
        try:
            num = task.get(timeout=1)
            print('Run task %d * %d' % (num, num))
            result_tmp = '%d * %d = %d' % (num, num, num * num)
            result.put(result_tmp)
        except Queue.Empty:
            print('Task queue is empty...')


if __name__ == '__main__':
    main()