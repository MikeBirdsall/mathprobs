""" Euler Problem 2 - sum of even-valued Fibonacci numberrs <= 4 million """

from timeit import timeit

def version1(limit=4000000):
    """ Brute force """
    total = 0
    first = 1
    second = 1
    while second < limit:
        if not second % 2 :
            total += second
        first, second = second, first + second
    return total

def version2(limit=4000000):
    """ Use only every third F number is even

        Since E+O=O, O+E=O, O+O=E sequence goes OOEOOEOOE...

    """
    total = 0
    first = 1
    second = 1
    third = first + second

    while second < limit:
        total = total + third
        first = second + third
        second = third + first
        third = first + second
    return total

def version3(limit=4000000):
    """ Use derived recursive relation for even or "third" F-numbers

        E(n)=4E(n)+E(n-2)
    """
    total = 2
    first = 2
    second = 8
    while second < limit:
        total += second
        first, second = second, 4 * second + first
    return total

def report(func):
    print("answer=%s msec=%6.3f" % (func(), timeit(func, number=1000)))


if __name__ == "__main__":
    for version in [version1, version2, version3]:
        report(version)
