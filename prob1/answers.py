""" Project Euler Prob 1 - find the sum of all multiples of 3 or 5 below 1000"""

from timeit import timeit

def version1(stop=1000):
    """ Brute Force Method """
    total = 0
    for x in range(1, stop):
        if x % 3 and x % 5:
            continue
        total += x
    return total

def version2(stop=1000):
    """ Brute force with list comprehension """
    return sum(x for x in range(1, stop) if not x % 3 or not x % 5)

def version3(top=1000):
    """ Use sum of consecutive integers formula"""

    def sum_divisible_by(factor):
        seq_length = (top - 1) // factor
        return factor * (seq_length * (seq_length + 1)) // 2

    return sum_divisible_by(3) + sum_divisible_by(5) - sum_divisible_by(15)

def report(func):
    print("answer=%s msec=%s" % (func(), timeit(func, number=1000)))


if __name__ == "__main__":
    for version in [version1, version2, version3]:
        report(version)
