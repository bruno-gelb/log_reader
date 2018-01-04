# todo measure processing time (timeit?.. consider multiprocessing)
# todo handle real log format (probably via regex for IPs)


def gather_unique_ips(input, output):
    unique_ips = set()  # todo maybe not the best choice, think about it

    with open(input, 'r') as f:
        pass
        # todo read unique_ips

    with open(output, 'w') as f:
        pass  # todo write unique_ips to output.txt


if __name__ == "__main__":
    # generate_big_sample(10 ** 7)
    gather_unique_ips(input='data/small_sample.txt',
                      output='output.txt')
