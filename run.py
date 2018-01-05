import os
from multiprocessing import Process
from timeit import default_timer as timer

from utils import sizeof_fmt

PROCESSES_NUMBER = 4  # later set it up to 4-8


def gather_unique_ips(input_file, output_file, worker_number):
    start = timer()
    unique_ips = set()

    offset = worker_number - 1

    with open(input_file, 'r') as f:
        for i, line in enumerate(f):
            if offset == PROCESSES_NUMBER - 1:
                offset = 0
            else:
                offset += 1
                continue

            ip = line.strip()  # todo handle real logfile format (probably via regex for IPs)
            print('Worker #{}, line {}'.format(worker_number, ip))
            unique_ips.add(ip)

    with open(output_file, 'w') as f:
        f.writelines('%s\n' % ip for ip in unique_ips)
    end = timer()

    # todo find out the better way to measure time in multiprocessing context =/
    print('Worker #{} finished in {:.2f} sec'.format(worker_number, end - start))


if __name__ == "__main__":
    # generate_big_sample(10 ** 7)

    input_file = 'data/small_sample_2.txt'
    output_file = 'output.txt'

    print('Text file ({0}) handling started..'.format(
        sizeof_fmt(os.path.getsize(input_file)))
    )

    jobs = []

    for i in range(PROCESSES_NUMBER):
        p = Process(target=gather_unique_ips,
                    args=(input_file, output_file, i + 1,))
        jobs.append(p)
        p.start()
