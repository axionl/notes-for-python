import subprocess
import time
import os



def run_sleep(period):
    proc = subprocess.Popen(['sleep', str(period)])
    return proc


def run_openssl(data):
    env = os.environ.copy()
    env['password'] = b'password'
    proc = subprocess.Popen(['openssl', 'enc', '-des3', '-pass', 'env:password'],
                            env=env, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    proc.stdin.write(data)
    proc.stdin.flush()  # Ensure the chile gets inputs
    return proc


def run_md5(input_stdin):
    proc = subprocess.Popen(['md5sum'], stdin=input_stdin, stdout=subprocess.PIPE)
    return proc


def main():
    proc = subprocess.Popen(['echo', 'Hello from the child!'], stdout=subprocess.PIPE)
    out, err = proc.communicate()
    if err is None:
        print(out.decode('utf-8'))

    proc = subprocess.Popen(['sleep', '0.3'])
    while proc.poll() is None:
        print('working')
    print('Exit status', proc.poll())

    start = time.time()
    procs = []
    for _ in range(10):
        proc = run_sleep(0.1)
        procs.append(proc)
    for proc in procs:
        proc.communicate()
    end = time.time()
    print('Finished in %.3f seconds' % (end - start))

    procs = []
    for _ in range(3):
        data = os.urandom(10)
        proc = run_openssl(data)
        procs.append(proc)
    for proc in procs:
        out, err = proc.communicate()
        if err is None:
            print(out[-10:])

    input_procs = []
    hash_procs = []
    for _ in range(3):
        data = os.urandom(10)
        proc = run_openssl(data)
        input_procs.append(proc)
        hash_proc = run_md5(proc.stdout)
        hash_procs.append(hash_proc)
    for proc in input_procs:
        proc.communicate()
    for proc in hash_procs:
        out, err = proc.communicate()
        if err is None:
            print(out.strip())

if __name__ == '__main__':
    main()
