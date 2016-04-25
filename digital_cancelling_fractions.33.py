'''
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

NOTE:
The product of these four fractions is (16/64 * 19/95 * 26/65 * 49/98) = 1/4 * 1/5 * 2/5 * 1/2 = 1/100
So, the result is 100.
'''

import math
import time


def is_digit_cancelling_fractions(v, a, b, c, d):
    precision = 10**-4
    if a == c:
        return abs(v - 1.0*b/d) < precision
    if a == d:
        return abs(v - 1.0*b/c) < precision
    if b == c:
        return abs(v - 1.0*a/d) < precision
    if b == d:
        return abs(v - 1.0*a/c) < precision

def main():
    start = time.time()
    for i in range(11, 100):
        if i % 10 != 0:
            for j in range(i+1, 100):
                if j % 10 != 0:
                    i1, i2, j1, j2 = i/10, i%10, j/10, j%10
                    value = 1.0*i/j
                    if is_digit_cancelling_fractions(value, i1, i2, j1, j2):
                        print i, j, value

    print "It costs:", time.time() - start, "seconds"

if __name__ == "__main__":
    main()
