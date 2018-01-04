# todo measure processing time (timeit?.. consider multiprocessing)
# todo handle real log format (probably via regex for IPs)


def gather_unique_ips(filename):
    pass
    # todo read and write unique IPs to output.txt


if __name__ == "__main__":
    # generate_big_sample(10 ** 7)
    gather_unique_ips('data/small_sample.txt')
