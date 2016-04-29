'''
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 * 7
15 = 3 * 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2**2 * 7 * 23
645 = 3 * 5 * 43
646 = 2 * 17 * 19.

Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?
'''

import math
import time
import profile


def is_prime(n):
    if n < 2: return False
    if n == 2: return True

    m = int(math.sqrt(n)) + 1
    for i in range(2, m):
        if n % i == 0:
            return False
    return True


def get_distinct_prime_factors(n):
    count = 0
    factors = []
    while not is_prime(n) and n != 1:
        for i in xrange(2, n/2+1):
            if n % i == 0:
                factors.append(i)
                n /= i
                break
    if n != 1:
        factors.append(n)
    return set(factors)



def main():
    '''sss'''
    start = time.time()
    print __doc__

    n = 100000 # finally is 134043
    while n < 300000:
        if 4==len(get_distinct_prime_factors(n)) \
            and 4==len(get_distinct_prime_factors(n+1)) \
            and 4==len(get_distinct_prime_factors(n+2)) \
            and 4==len(get_distinct_prime_factors(n+3)):
            print n, get_distinct_prime_factors(n), get_distinct_prime_factors(n+1), get_distinct_prime_factors(n+2), get_distinct_prime_factors(n+3)
            break
        else:
            n += 1

    print "#### Another awesome solution (less than 0.1 second) ####"
    LIMIT = 200000 # since I have already know the result
    factors = [0] * LIMIT
    count = 0
    for i in xrange(2, LIMIT):
        if factors[i] == 0:
            count = 0
            val = i
            while val < LIMIT:
                factors[val] += 1
                val += i
        elif factors[i] == 4:
            count += 1
            if count == 4:
                print i - 3
                break
        else:
            count = 0

    print "It costs:", time.time() - start, "seconds"

if __name__ == "__main__":
    profile.run("main()")
