""" Euler Problem 5 - Smallest multiple

    2520 is the smallest number that can be divided by each of the numbers
    from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by all of
    the numbers from 1 to 20?

    Version 1: Pure brute force

    """

from argparse import ArgumentParser
from timeit import timeit
from math import log, sqrt


class base_version(object):

    def __init__(self):
        pass

    def debug(self):
        print("answer=%s" % (self.run()))

    def timing(self, number):
        print("microsec=%6.3f" % (timeit(self.run, number=1000 * number)/number))

    def report(self, number):
        print("Version: {} answer={} msec={:6.3f}".format(
            self.__class__.__name__, self.run(),
            10 * timeit(self.run, number=100*number)/number))

    def run(self):
        raise NotImplementedError


class version1(base_version):

    def run(self):
        x = 19
        while True:
            x += 1
            for factor in range(2,20):
                if x % factor:
                    break
            else:
                return x

class version2(base_version):

    def run(self):
        base = 16 * 9 * 5 * 7 * 11 * 13 * 17 * 19
        x = 0
        while True:
            x += base
            for factor in range(2, 20):
                if x % factor:
                    break
            else:
                return x

class version3(base_version):

    def run(self):
        p = [2, 3, 5, 7, 11, 13, 17, 19]
        a = []
        k = 20
        N = 1
        log_k = log(k)
        limit = sqrt(20)
        for i, prime in enumerate(p):
            if prime < limit:
                a.append(int(log_k / log(prime)))
            else:
                a.append(1)
            N = N * prime ** a[i]
        return N



if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--time", type=int,
        help="Time running the versions")
    parser.add_argument("--report", type=int, help="report answer and timing")
    args = parser.parse_args()


    for version in (version2(), version3()):
        if args.time:
            version.timing(args.time)
        elif args.report:
            version.report(args.report)
        else:
            version.debug()


