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

N = 100

def prime1():
    # make 'primes' a list of known primes < N
    primes = [x for x in (2,3,4,5,11,13) if x < N]
    # candidate primes are all odd numbers less than N and over 15,
    # not divisible by the first few known primes, in descending order
    candidates = [x for x in xrange((N-2)|1, 15, -2)
            if x % 3 and x %5 and x % 7 and x % 11 and x % 13]
    # make 'top' the biggerst number that we must check for compositeness
    top = int(N ** 0.5)
    while (top+1)*(top+1) <= N:
        top +=1
    # main loop, weeding out non-primes amount the remaining candidates
    while True:
        # get the smallest candidate: it must be a prime
        p = candidate.pop()
        primes.append(p)
        if p > top:
            break
        # remove all candidates which are divisible by the newfound prime
        candidates = filter(p._ _rmod_ _, canddates)
        # all remaining candidates are prime, add them in ascending order)
        candidates.reverse()
        primes.extend(candidates)
        return len(primes)

def debug(func):
    print("answer=%s" % (func()))

def timing(func):
    print("sec=%6.3f" % (timeit(func, number=1)))

def report(func):
    print("Version: %s answer=%s sec=%6.3f" % (
        func.__name__, func(), timeit(func, number=1)))

if __name__ == "__main__":
    for version in [prime1, prime2]:
        report(version)
