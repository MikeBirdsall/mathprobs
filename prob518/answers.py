""" Euler Problem 518 - Prime triples and geometric sequences

    Let S(n) = a+b+c over all triples (a,b,c) such that:

    - a,b,and c are prime numbers.
    - a < b < c < n
    - a+1,b+1, and c+1 form a geometric sequence.

    For example, S(100) = 1035 with the following triples:

    (2,5,11),(2,11,47),(5,11,23),(5,17,53),(7,11,17),(7,23,71),(11,23,47),
    (17,23,31),(17,41,97),(31,47,71),(71,83,97)

"""

from timeit import timeit
from itertools import repeat
from math import sqrt
import cProfile


class primes(object):
    def __init__(self, upper_bound):
        isprime = self.isprime = list(repeat(1, upper_bound+2))
        isprime[0] = isprime[1] = 0
        index = 2
        sqrt_ub = sqrt(upper_bound)
        while index < sqrt_ub:
            isprime[index] = 1
            multiple = index * 2
            while multiple <= upper_bound:
                isprime[multiple] = 0
                multiple += index
            index = isprime.index(1, index+1)

class version1(object):
    def __init__(self, upper_bound):
        self.isprime = primes(upper_bound)
        self.upper_bound = upper_bound

    def run(self):
        isprime = self.isprime.isprime
        total = 0
        a = 0
        while a < self.upper_bound:
            a = isprime.index(1, a+1)
            numanswers = 0
            b = a
            while b < self.upper_bound:
                b = isprime.index(1, b+1)
                c = ((b + 1) * (b + 1) / (a + 1)) - 1
                if c > self.upper_bound:
                    break
                if not c.is_integer() or not isprime[int(c)]:
                    continue
                c = int(c)
                #print(a, b, c, (b+1)/(a+1))
                total += sum((a, b, c))
                numanswers += 1
            print("Prime %s has %s triples." % (a, numanswers))

        return total

def debug(func):
    print("answer=%s" % (func(int(1e8)).run()))

def timing(func):
    print("sec=%6.3f" % (timeit(func, number=1)))

def report(func):
    print("Version: %s answer=%s sec=%6.3f" % (
        func.__name__, func(), timeit(func, number=1)))

if __name__ == "__main__":
    for version in [version1]:
        cProfile.run('version1(int(1e5)).run()')
        #debug(version)