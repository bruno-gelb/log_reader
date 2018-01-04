# todo measure processing time (timeit, clockit?.. consider multiprocessing)
# todo handle real log format (probably via regex for IPs)

import os
from timeit import default_timer as timer

from utils import sizeof_fmt


def gather_unique_ips(input_file, output_file):
    unique_ips = set()

    with open(input_file, 'r') as f:
        for line in f:
            unique_ips.add(line.strip())

    with open(output_file, 'w') as f:
        f.writelines('%s\n' % ip for ip in unique_ips)


if __name__ == "__main__":
    # generate_big_sample(10 ** 7)

    input_file = 'data/big_sample.txt'
    output_file = 'output.txt'

    start = timer()
    gather_unique_ips(input_file, output_file)

    end = timer()
    print('Text file with size {0} was handled in {1:.2f} sec'.format(
        sizeof_fmt(os.path.getsize(input_file)), end - start)
    )
