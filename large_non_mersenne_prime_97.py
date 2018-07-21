# -*- coding:utf-8 -*-
'''
Large non-Mersenne prime
Problem 97 
The first known prime found to exceed one million digits was discovered in 1999, and is a Mersenne prime of the form 26972593−1; it contains exactly 2,098,960 digits. Subsequently other Mersenne primes, of the form 2p−1, have been found which contain more digits.

However, in 2004 there was found a massive non-Mersenne prime which contains 2,357,207 digits: 28433×27830457+1.

Find the last ten digits of this prime number.
'''

import profile
import time


def last_ten_digits(n):
    if n <= 33:
        return 2**n
    if n % 2 == 0:
        tmp = last_ten_digits(n/2)
        return tmp*tmp % 10000000000
    else:
        tmp = last_ten_digits(n/2)
        return tmp*tmp*2 % 10000000000


def main():
    start = time.time()
    print __doc__
    print "####### result below #######"

    print last_ten_digits(7830457)
    print (9700303872 * 28433 + 1) % 10000000000

    print "####### result done #######"
    print "It costs:", time.time() - start, "seconds"


if __name__ == "__main__":
    profile.run("main()")
