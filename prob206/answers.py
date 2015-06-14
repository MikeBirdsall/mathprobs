""" Euler Problem 206 - Find integer whose square is 1_2_3_4_5_6_7_8_9_0

    Smallest square is 1020304050607080900
    Largest square is  1929394959697989990

    answer n: 1010101010 < n < 1389026624 or about 380 million possibilities.

    But the answer much have a factor of 10 for the square to have a factor
    of ten. Which means the square will have a factor of 100, and have the
    form 1_2_3_4_5_6_7_8_900.


"""

from timeit import timeit
import re
from collections import deque

def version1():
    pattern = re.compile('1\d2\d3\d4\d5\d6\d7\d8\d9\d0')
    for answer in range(1010101010, 1389026630, 10):
        square = str(answer * answer)
        if pattern.match(str(square)):
            return answer
    return 'failed'

def version2():
    """ Is regular expression too slow? """
    for answer in range(1010101010, 1389026630, 10):
        square = str(answer * answer)
        if (
            square[0] == '1' and
            square[2] == '2' and
            square[4] == '3' and
            square[6] == '4' and
            square[8] == '5' and
            square[10] == '6' and
            square[12] == '7' and
            square[14] == '8' and
            square[16] == '9' and
            square[18] == '0'):
            return answer
    return 'failed'

def version3():
    """ Is regular expression too slow? """
    for answer in range(1010101010, 1389026630, 10):
        square = str(answer * answer)
        if square[::2] == '1234567890':
            return answer
    return 'failed'

def version4():
    """ Factor out the power of 10 - no real speed improvement """
    for answer in range(101010101, 138902663):
        square = str(answer * answer)
        if (square[0] == '1' and
            square[2] == '2' and
            square[4] == '3' and
            square[6] == '4' and
            square[8] == '5' and
            square[10] == '6' and
            square[12] == '7' and
            square[14] == '8' and
            square[16] == '9'):
            return answer * 10
    return 'failed'

def version5():
    """ Factor more out

        Since the square ends in 900, the answer must end in 30 or 70
    """

    for answer in range(101010100, 138902660, 10):
        for end in [3, 7]:
            with_end = answer + end
            square = str(with_end * with_end)
            if (square[0] == '1' and
                    square[2] == '2' and
                    square[4] == '3' and
                    square[6] == '4' and
                    square[8] == '5' and
                    square[10] == '6' and
                    square[12] == '7' and
                    square[14] == '8' and
                    square[16] == '9'):
                return with_end * 10
    return 'failed'

def version6():
    """ Compute one digit at a time """
    maxsquare = 1929394959697989990
    patterns = [re.compile(y) for y in (
        '',
        '0',
        '\d0',
        '9\d0',
        '\d9\d0',
        '8\d9\d0',
        '\d8\d9\d0',
        '7\d8\d9\d0',
        '\d7\d8\d9\d0',
        '6\d7\d8\d9\d0',
        '\d6\d7\d8\d9\d0',
        '5\d6\d7\d8\d9\d0',
        '\d5\d6\d7\d8\d9\d0',
        '4\d5\d6\d7\d8\d9\d0',
        '\d4\d5\d6\d7\d8\d9\d0',
        '3\d4\d5\d6\d7\d8\d9\d0',
        '\d3\d4\d5\d6\d7\d8\d9\d0',
        '2\d3\d4\d5\d6\d7\d8\d9\d0',
        '\d2\d3\d4\d5\d6\d7\d8\d9\d0',
        '1\d2\d3\d4\d5\d6\d7\d8\d9\d0',
    )]

    # Set first digit
    sofar = deque(['30', '70'])

    answer = 'notfound'
    while sofar:
        attempt = sofar.pop()
        digits = len(attempt) + 1
        pattern = patterns[digits]
        for digit in range(10):
            _try = str(digit) + attempt
            tryint = int(_try)
            squareint = tryint * tryint
            if squareint > maxsquare:
                break
            square = str(squareint).zfill(19)
            if pattern.match(square[-digits:]):
                if patterns[19].match(square):
                    answer = tryint
                    return answer
                sofar.append(_try)
                if digits > 9:
                    for x in range(11, 20):
                        if not patterns[x].match(square[-x:]):
                            break
    return answer

def debug(func):
    print("answer=%s" % (func()))

def timing(func):
    print("sec=%6.3f" % (timeit(func, number=1)))

def report(func):
    print("Version: %s answer=%s sec=%6.3f" % (
        func.__name__, func(), timeit(func, number=1)))

if __name__ == "__main__":
    for version in [version1, version2, version3, version4, version5,
            version6]:
        report(version)
