import os
from multiprocessing import Process
from timeit import default_timer as timer

import redis

from utils import sizeof_fmt

PROCESSES_NUMBER = 4


# @profile()
def gather_unique_ips(input_file, worker_number):
    worker_start = timer()

    offset = worker_number - 1

    with open(input_file, 'r') as f:
        for i, line in enumerate(f):
            if offset == PROCESSES_NUMBER - 1:
                offset = 0
            else:
                offset += 1
                continue

            ip = line.strip()  # todo handle real logfile format (probably via regex for IPs)

            # todo this part is taking all the time. Try to optimize it
            r.set(ip, '')

    worker_end = timer()

    print('Worker #{} finished in {:.2f} sec.'.format(worker_number, worker_end - worker_start))


if __name__ == "__main__":
    # generate_sample(10 ** 7, 'huge_sample.txt')

    r = redis.StrictRedis(host='localhost', port=6379, db=0,
                          charset="utf-8", decode_responses=True)
    r.flushall()

    input_file = 'data/big_sample.txt'
    # input_file = 'data/huge_sample.txt'

    print('Text file ({0}) handling started ..'.format(
        sizeof_fmt(os.path.getsize(input_file)))
    )

    jobs = []
    start = timer()

    for i in range(PROCESSES_NUMBER):
        p = Process(target=gather_unique_ips,
                    args=(input_file, i + 1,))
        jobs.append(p)
        p.start()

    for job in jobs:
        job.join()

    end = timer()

    unique_ips = r.keys()

    print('All workers finished in {:.2f} sec.'.format(end - start))
    print('{} unique IPs found.'.format(len(unique_ips)))

    with open('output.txt', 'w') as f:
        f.writelines('%s\n' % ip for ip in unique_ips)
