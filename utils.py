import os
from random import randrange


def sizeof_fmt(num, suffix='B'):
    # stackoverflow.com/a/1094933
    for unit in ['', 'K', 'M', 'G', 'T', 'P', 'E', 'Z']:
        if abs(num) < 1024.0:
            return "%3.1f %s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f %s%s" % (num, 'Yi', suffix)


def generate_ip():
    # codingwithcody.com/2010/07/03/generate-random-ip-with-python/
    not_valid = [10, 127, 169, 172, 192]

    first = randrange(1, 256)
    while first in not_valid:
        first = randrange(1, 256)

    ip = ".".join([str(first), str(randrange(1, 256)),
                   str(randrange(1, 256)), str(randrange(1, 256))])
    return ip


def generate_sample(lines_amount, filename):
    filename = os.path.join(os.getcwd(), 'data', filename)
    with open(filename, 'w') as f:
        for i in range(lines_amount):
            # todo write in bulk instead. Speed is okay tho since it's one-time generation
            print(generate_ip(), file=f)
