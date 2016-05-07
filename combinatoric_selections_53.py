'''
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general,
nCr = n! / r!(n-r)!, where r <= n
It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of  nCr, for 1 <= n <= 100, are greater than one-million?
'''

import math
import time
import profile


def factorial(x):
    ret = 1
    for i in range(1, x+1):
        ret *= i
    return ret


def get_nCr(n, r):
    return factorial(n) / (factorial(r) * factorial(n-r))


def main():
    '''sss'''
    start = time.time()
    print __doc__

    count = 0
    for i in range(23, 101):
        for j in range(2, i-1):
            if get_nCr(i, j) > 1000000:
                count += 1
    print count

    print "It costs:", time.time() - start, "seconds"

if __name__ == "__main__":
    profile.run("main()")
