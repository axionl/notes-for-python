import threading

local_school = threading.local()

def process_student():
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))


def process_thread(name):
    local_school.student = name
    process_student()


def main():
    thread1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
    thread2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')

    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()


if __name__ == '__main__':
    main()