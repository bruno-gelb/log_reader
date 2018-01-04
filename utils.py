import os
from random import randrange


def generate_ip():
    # codingwithcody.com/2010/07/03/generate-random-ip-with-python/
    not_valid = [10, 127, 169, 172, 192]

    first = randrange(1, 256)
    while first in not_valid:
        first = randrange(1, 256)

    ip = ".".join([str(first), str(randrange(1, 256)),
                   str(randrange(1, 256)), str(randrange(1, 256))])
    return ip


def generate_big_sample(lines_amount):
    filename = os.path.join(os.getcwd(), 'data', 'big_sample.txt')
    with open(filename, 'w') as f:
        for i in range(lines_amount):
            # todo write in bulk instead. Speed is okay tho since it's one-time generation
            print(generate_ip(), file=f)
