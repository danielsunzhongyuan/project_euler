'''
n! = n*(n-1)*(n-2)*...*3*2*1
For example, 10! = 10*9*8*...*3*2*1 = 3628800
and sum of the digits in the number is 3+6+2+8+8+0+0=27.

Find the sum of the digits in the number 100!
'''

import math
import time
from functools import wraps

def memo(func):
    cache = {}
    @wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap

def fac(n):
    if n == 1:
        return 1
    return n * fac(n-1)

def fac_2(n, result):
    while len(result) < n:
        result.append((len(result) + 1)*result[-1])
    return result[-1]

def fac_3(n):
    a = 1
    result = 1
    while a <= n:
        result *= a
        yield result
        a += 1

def main():
    start = time.time()
    # This func should not work because "maximum recursion depth exceeded"
    print sum([int(i) for i in str(fac(10000))])
    print "It costs:", time.time() - start, "seconds"

    # This func costs about 0.097 seconds
    result = [1]
    x = fac_2(10000, result)
    print sum([int(i) for i in str(x)])
    print "It costs:", time.time() - start, "seconds"

    # This func costs about 0.065 seconds
    for i in fac_3(10000):
        y = i
    print sum([int(i) for i in str(y)])
    print "It costs:", time.time() - start, "seconds"


if __name__ == "__main__":
    main()
