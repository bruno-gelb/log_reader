# todo handle real logfile format (probably via regex for IPs)

import os
from multiprocessing import Process
from timeit import default_timer as timer

from utils import sizeof_fmt

PROCESSES_NUMBER = 2  # later set it up to 8


def gather_unique_ips(input_file, output_file, worker_number):
    start = timer()
    unique_ips = set()

    with open(input_file, 'r') as f:
        for line in f:
            unique_ips.add(line.strip())

    with open(output_file, 'w') as f:
        f.writelines('%s\n' % ip for ip in unique_ips)
    end = timer()

    # todo find out the better way to measure time in multiprocessing context =/
    print('Worker #{} finished in {} sec'.format(worker_number, end - start))


if __name__ == "__main__":
    # generate_big_sample(10 ** 7)

    input_file = 'data/big_sample.txt'
    output_file = 'output.txt'

    print('Text file ({0}) handling started..'.format(
        sizeof_fmt(os.path.getsize(input_file)))
    )

    jobs = []

    for i in range(PROCESSES_NUMBER):
        p = Process(target=gather_unique_ips,
                    args=(input_file, output_file, i,))
        jobs.append(p)
        p.start()
