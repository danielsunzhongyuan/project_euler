'''
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2*12
15 = 7 + 2*22
21 = 3 + 2*32
25 = 7 + 2*32
27 = 19 + 2*22
33 = 31 + 2*12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
'''

import math
import time
import profile


def is_prime(n):
    if n < 2: return False
    if n == 2: return True
    square = int(math.sqrt(n))
    for i in xrange(2, square + 1):
        if n % i == 0:
            return False
    return True


def main():
    '''sss'''
    start = time.time()
    print __doc__

    n = 33
    isGoldbach = True
    while isGoldbach:
        if is_prime(n):
            n += 2
            continue
        square = int(math.sqrt(n/2))
        for i in xrange(square, 0, -1):
            if is_prime(n - 2*i*i):
                break
        if i == 1 and not is_prime(n-2):
            isGoldbach = False
        else:
            n += 2
    print n

    print "It costs:", time.time() - start, "seconds"

if __name__ == "__main__":
    profile.run("main()")
