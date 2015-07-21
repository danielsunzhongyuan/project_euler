'''
Euler discovered the remarkable quadratic formula:
                  n^2 + n + 41
It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.

The incredible formula  n^2 - 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, -79 and 1601, is -126479.

Considering quadratics of the form:

n^2 + an + b, where |a| < 1000 and |b| < 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |-4| = 4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.

NOTE:
Better solution:
1. when n=0, n^2+a*n+b = b, so b must be a prime
2. if b is 2:
    n = 1, n^2+a*n+b = 1+a+2 = 3+a, then a should be -1 or 2 or 4 or ...
    n = 2, n^2+a*n+b = 6+2a, then a should be -2
3. Therefore, it would not has too many primes to generate if b equals 2.
4. Therefore, b would be 3, 5, 7, 11 ... (all odd)
5. when n=1, n^2+a*n+b = 1+a+b, then a should be an odd number
So, range of a is range(-999, 1000, 2), range of b is [3, 5, 7, 11,...,1000)

The running time improves from 4.03 seconds to 0.76 seconds.
'''

import math
import time
import imp

def main():
    start = time.time()
    with open('max_prime_factor.3.py', 'rb') as fp:
        mod = imp.load_module(
            'isPrime', fp, 'max_prime_factor.3.py',
            ('.py', 'rb', imp.PY_SOURCE)
        )
    primes = [i for i in range(3, 1000) if mod.isPrime(i)]
    max_a, max_b, max_n = 0, 0, 0
    for a in range(-999, 1000, 2):
        for b in primes:
            n = 0
            while mod.isPrime(n*n + a*n + b):
                n += 1
            if n > max_n:
                max_a, max_b, max_n = a, b, n
    print max_a, max_b, max_n

    print "It costs:", time.time() - start, "seconds"

if __name__ == "__main__":
    main()
