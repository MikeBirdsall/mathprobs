""" Euler Problem 53 - Count values of C(n,r) > 1000000, for 1<=n<=100 """

from math import factorial
from timeit import timeit

def version1():
    count = 0
    for n in range(1, 101):
        for r in range(1, n+1):
            if factorial(n) / (factorial(r) * factorial(n-r)) > 1000000:
                count += 1

    return count

def version2():
    f = [1]
    for i in range(1, 101):
        f.append(f[-1]*i)

    count = 0
    for n in range(1, 101):
        for r in range(1, n+1):
            if f[n] / (f[r] * f[n-r]) > 1000000:
                count += 1
    return count

def version2a():
    f = [factorial(x) for x in range(101)]

    count = 0
    for n in range(1, 101):
        for r in range(1, n+1):
            if f[n] / (f[r] * f[n-r]) > 1000000:
                count += 1
    return count

def version2b():
    def mem_fact(n, _cache={0: 1, 1: 1, 'max': 1}):
        if n <= _cache['max']:
            return _cache[n]

        for x in range(_cache['max']+1, n+1):
            _cache[x] = _cache[x-1] * x
            _cache['max'] = n
        return _cache[n]

    count = 0
    for n in range(1, 101):
        for r in range(1, n+1):
            if mem_fact(n) / (mem_fact(r) * mem_fact(n-r)) > 1000000:
                count += 1
    return count


def report(func):
    print("answer=%s msec=%6.3f" % (func(), 10 * timeit(func, number=100)))

if __name__ == "__main__":
    for version in [version2b, version1, version2, version2a]:
        report(version)


