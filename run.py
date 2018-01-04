# todo measure processing time (timeit?.. consider multiprocessing)
# todo handle real log format (probably via regex for IPs)


def gather_unique_ips(input_file, output_file):
    unique_ips = set()

    with open(input_file, 'r') as f:
        for line in f:
            unique_ips.add(line.strip())

    with open(output_file, 'w') as f:
        f.writelines('%s\n' % ip for ip in unique_ips)


if __name__ == "__main__":
    # generate_big_sample(10 ** 7)
    gather_unique_ips(input_file='data/small_sample.txt',
                      output_file='output.txt')
