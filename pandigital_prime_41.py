'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?

Analyze: a 9-digit pandigital number would not be a prime, because 1+2+3+...+9 = 45, which means it would never be a prime
therefore, only 7-digit number or 4-digit number could be a prime.
So, two solutions:
1. get all permulations, then find primes
2. find all primes, then find permulations

'''

import math
import time
import profile


def is_pandigital_number(n):
    return "0" not in str(n) and len(set(str(n))) == len(str(n)) and int(max(set(str(n)))) == len(str(n))


def is_prime(n):
    if n < 2: return False
    if n == 2 or n == 3: return True
    if n % 2 == 0: return False

    if sum([int(x) for x in str(n)]) % 3 == 0: return False
    end = int(math.sqrt(n)) + 1
    for i in range(3, end):
        if n % i == 0:
            return False
    return True


def main():
    start = time.time()
    print __doc__

    for x in range(1233, 4322, 2):
        if is_pandigital_number(x) and is_prime(x):
            print x
    for x in range(7654321, 1234566, -2):
        if is_pandigital_number(x) and is_prime(x):
            print x
            break

    print "It costs:", time.time() - start, "seconds"

if __name__ == "__main__":
    profile.run("main()")
