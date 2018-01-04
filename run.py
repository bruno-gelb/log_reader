# todo measure processing time (timeit?.. consider multiprocessing)
# todo handle real log format (probably via regex for IPs)


def gather_unique_ips(input, output):
    unique_ips = set()

    with open(input, 'r') as f:
        for line in f:
            unique_ips.add(line.strip())

    with open(output, 'w') as f:
        f.writelines('%s\n' % ip for ip in unique_ips)


if __name__ == "__main__":
    # generate_big_sample(10 ** 7)
    gather_unique_ips(input='data/small_sample.txt',
                      output='output.txt')
