""" Euler Problem 3 - find largest prime factor of 600851475143 """

from timeit import timeit
from math import sqrt

def version1(n=600851475143):
    factor = 2
    last_factor = 1
    while n > 1:
        if not n % factor:
            last_factor = factor
            n = n // factor
            while not n % factor:
                n = n // factor
        factor = factor + 1
    return last_factor

def version2(n=600851475143):
    """ Special case 2, so you can halve the steps """
    if n % 2:
        last_factor = 1
    else:
        n = n // 2
        last_factor = 2
        while not n % 2:
            n = n // 2

    factor = 3
    while n > 1:
        if not n % factor:
            n = n // factor
            last_factor = factor
            while not n % factor:
                n = n // factor
        factor = factor + 2
    return last_factor

def version3(n=600851475143):
    """ We can stop when we hit square-root of n """
    if n % 2:
        last_factor = 1
    else:
        n = n // 2
        last_factor = 2
        while not n % 2:
            n = n // 2

    factor = 3
    max_factor = int(sqrt(n))
    while n > 1 and factor <= max_factor:
        if not n % factor:
            n = n // factor
            last_factor = factor
            while not n % factor:
                n = n // factor
            max_factor = int(sqrt(n))
        factor = factor + 2
    if n == 1:
        return last_factor
    else:
        return n

def report(func):
    print("answer=%s msec=%6.3f" % (func(), timeit(func, number=1000)))


if __name__ == "__main__":
    for version in [version1, version2, version3]:
        report(version)
