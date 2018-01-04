# todo consider multiprocessing in measuring time
# todo handle real logfile format (probably via regex for IPs)

import os
from multiprocessing import Process
from timeit import default_timer as timer

from utils import sizeof_fmt

PROCESSES_NUMBER = 2  # later set it up to 8


def gather_unique_ips(input_file, output_file, offset):
    unique_ips = set()

    with open(input_file, 'r') as f:
        for line in f[::offset]:
            unique_ips.add(line.strip())

    with open(output_file, 'w') as f:
        f.writelines('%s\n' % ip for ip in unique_ips)


if __name__ == "__main__":
    # generate_big_sample(10 ** 7)

    input_file = 'data/small_sample.txt'
    output_file = 'output.txt'

    jobs = []
    start = timer()
    for i in range(PROCESSES_NUMBER):
        p = Process(target=gather_unique_ips,
                    args=(input_file, output_file, i,))
        jobs.append(p)
        p.start()
    end = timer()

    print('Text file with size {0} was handled in {1:.2f} sec'.format(
        sizeof_fmt(os.path.getsize(input_file)), end - start)
    )
