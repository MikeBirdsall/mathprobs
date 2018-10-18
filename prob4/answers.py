""" Euler Problem 4 - Find largest palindrome product of two 3-digit numbers.

    A palindromic number reads the same both ways. The largest palindrome
    made from the product of two 2-digit numbers is 9009 = 91 * 99.

    Find the largest palindrome made from the product of two 3-digit numbers.

    Version 1: Pure brute force
    Version 2: Loop through smaller and larger factor, don't duplicate
    Version 3: Start with largest factors and truncate when too small
    Version 4: factorization
        A palindrome of two 3-digit numbers is 5 or 6 digits.
        If it's 6 digits, then it is of the form abccba
        which can be expressed as
        100000a + 10000b + 1000c + 100c + 10b + 1a =
        11(9091a + 910b + 100c)

        so one of the factors is divisible by 11. Make that the outer loop
        (instead of the larger factor).
        If you don't find a palindrome it must be a five digit, and must use
        a different method
    Version 5: Make outer loop largest, but adjust inner to get 11 factor

    """

from argparse import ArgumentParser
from timeit import timeit


class base_version(object):

    def __init__(self):
        pass

    def debug(self):
        print("answer=%s" % (self.run()))

    def timing(self, number):
        print("sec=%6.3f" % (timeit(self.run, number=number)/number))

    def report(self, number):
        print("Version: {} answer={} sec={:6.3f}".format(
            self.__class__.__name__, self.run(),
            timeit(self.run, number=number)/number))

    def is_palindrome(self, candidate):
        z = str(candidate)
        return z == z[::-1]

    def run(self):
        raise NotImplementedError


class version1(base_version):

    def run(self):
        maxpal = 0
        for x in range(100,1000):
            for y in range(100,1000):
                z = x * y
                if z > maxpal and self.is_palindrome(z):
                    maxpal = z
                    max_x = x
                    max_y = y
        return maxpal

class version2(base_version):

    def run(self):
        maxpal = 0
        for x in range(100,1000):
            for y in range(x, 1000):
                z = x * y
                if z > maxpal and self.is_palindrome(z):
                    maxpal = z
        return maxpal

class version3(base_version):

    def run(self):
        maxpal = 0
        for x in range(999,99,-1):
            for y in range(x, 99, -1):
                z = x * y
                if z < maxpal:
                    break
                if self.is_palindrome(z):
                    maxpal = z
                    break
        return maxpal

class version4(base_version):

    def run(self):
        maxpal = 0
        for x in range(990,99,-11):
            for y in range(999, 99, -1):
                z = x * y
                if z < maxpal:
                    break
                if self.is_palindrome(z):
                    maxpal = z
                    break
        return maxpal

class version5(base_version):

    def run(self):
        maxpal = 0
        for x in range(999,99,-1):
            if x % 11:
                for y in range(999, x, -1):
                    z = x * y
                    if z < maxpal:
                        break
                    if self.is_palindrome(z):
                        maxpal = z
                        break
            else:
                for y in range(990, x, -11):
                    z = x * y
                    if z < maxpal:
                        break
                    if self.is_palindrome(z):
                        maxpal = z
                        break
        return maxpal

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--time", type=int,
        help="Time running the versions")
    parser.add_argument("--report", type=int, help="report answer and timing")
    args = parser.parse_args()


    for version in (version1(), version2(), version3(), version4(), version5()):
        if args.time:
            version.timing(args.time)
        elif args.report:
            version.report(args.report)
        else:
            version.debug()


