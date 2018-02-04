"""MapReduce."""

from threading import Thread
from assertpy import assert_that
from tempfile import TemporaryDirectory
import logging
import os

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

logger = logging.getLogger(__name__)

class InputData(object):
    def read(self):
        raise NotImplementedError

# class GenericInputData(object):
#     def read(self):
#         raise NotImplementedError

#     @classmethod
#     def generate_inputs(cls, config):
#         raise NotImplementedError

# class PathInputData(GenericInputData):
#     def read(self):
#         return open(self.path).read()

#     @classmethod
#     def generate_inputs(cls, config):
#         data_dir = config['data_dir']
#         for name in os.listdir(data_dir):
#             yield cls(os.path.join(data_dir, name))

class PathInputData(InputData):
    def __init__(self, path):
        super().__init__()
        self.path = path

    def read(self):
        data = open(self.path).read()
        return data

class Worker(object):
    def __init__(self, input_data):
        self.input_data = input_data
        self.result = None
    
    def map(self):
        raise NotImplementedError

    def reduce(self, other):
        raise NotImplementedError

class LineCountWorker(Worker):
    def map(self):
        data = self.input_data
        self.result = data.count('\n')
        result = self.result
        return result

    def reduce(self, other):
        self.result += other.result

def generate_inputs(data_dir):
    for name in os.listdir(data_dir):
        path = os.path.join(data_dir, name)
        result = PathInputData(path)
        yield result.read()

def create_workers(input_list):
    workers = []
    for input_data in input_list:
        workers.append(LineCountWorker(input_data).map())
    return workers

def execute(workers):
    #Todo: Learn how does multi-thread work.

    # threads = [Thread(target=w.map) for w in workers]
    # for thread in threads:
    #     thread.start()

    # for thread in threads:
    #     thread.join()

    # first, rest = workers[0], workers[1:]
    # for worker in rest:
    #     first.reduce(worker)
    # return first.result
    result = sum(workers)  # insteaf of reduce
    return result

def mapreduce(data_dir):
    inputs = generate_inputs(data_dir)
    workers = create_workers(inputs)
    return execute(workers)

def write_test_file(tmpdir):
    test_data = ''
    for i in range(5):
        test_data += '1, 2, 3, 4, 5, 6\n'
    try:
        for i in range(10):
            with open(tmpdir + 'test-%s.txt' % i, 'w+') as f:
                f.write(test_data)
        return True
    except IOError:
        return False
    
def main():
    tmpdir = './'
    if write_test_file(tmpdir):
        result = mapreduce(tmpdir)
    else:
        print('File I/O Error')
 
    
    print('There are', result, 'lines')

if __name__ == '__main__':
    main()
    
