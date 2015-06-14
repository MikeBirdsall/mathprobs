""" Euler Problem 49 - Arithmetic sequence of 3 4 digit primes which are
    permutations of each other


    The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
    increases by 3330, is unusual in two ways: (i) each of the three terms are
    prime, and, (ii) each of the 4-digit numbers are permutations of one
    another.

    There are no arithmetic sequences made up of three 1-, 2-, or 3-digit
    primes, exhibiting this property, but there is one other 4-digit
    increasing sequence.

    What 12-digit number do you form by concatenating the three terms in this
    sequence?

"""

from timeit import timeit

primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61,
    67, 71, 73, 79, 83, 89, 97]

def version1():
    # Loop for smallest answer (4 digit prime with room for 2 more)
    for x in range(1009, 9974, 2):
        # Loop through possible increments
        for y in range(2, 5000, 2):
            tries = (x, x+y, x+y+y)
            if tries[2] >= 10000:
                break
            stries = list(map(str, tries))

            # Check that they are permutations by sorting digits
            if len(set(map(''.join, map(sorted, stries)))) > 1:
                continue
            # Or, equivalently
            # if len(set(''.join(sorted(x)) for x in stries)) > 1:

            # Test for primes under 10000
            if any(1 for x in tries for z in primes if not x % z):
                continue

            # Don't count the given answer
            if tries[0] != 1487:
                return ''.join(stries)

def version2():
    # Loop for smallest answer (4 digit prime with room for 2 more)
    for x in range(1009, 9974, 2):
        # Loop through possible increments
        for y in range(18, 5000, 18):
            tries = (x, x+y, x+y+y)
            if tries[2] >= 10000:
                break
            stries = list(map(str, tries))

            # Check that they are permutations by sorting digits
            if len(set(map(''.join, map(sorted, stries)))) > 1:
                continue
            # Or, equivalently
            # if len(set(''.join(sorted(x)) for x in stries)) > 1:

            # Test for primes under 10000
            if any(1 for x in tries for z in primes if not x % z):
                continue

            # Don't count the given answer
            if tries[0] != 1487:
                print(tries)
                return ''.join(stries)


def debug(func):
    print("answer=%s" % (func()))

def timing(func):
    print("sec=%6.3f" % (timeit(func, number=1)))

def report(func):
    print("Version: %s answer=%s sec=%6.3f" % (
        func.__name__, func(), timeit(func, number=1)))

if __name__ == "__main__":
    for version in [version1, version2]:
        report(version)

