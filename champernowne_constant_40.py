'''
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 * d10 * d100 * d1000 * d10000 * d100000 * d1000000
'''

import math
import time
import profile


def get_nth_digit(n):
    if n < 1:
        return 0
    i = 1
    while n > i*9*10**(i-1):
        n -= i*9*10**(i-1)
        i += 1

    divider, remainder = divmod(n, i)
    if remainder == 0:
        number = divider + 10**(i-1) - 1
        return str(number)[-1]
    else:
        number = divider + 10**(i-1) + 1
        return str(number)[remainder-1]


def main():
    start = time.time()
    print __doc__

    print "It costs:", time.time() - start, "seconds"

if __name__ == "__main__":
    profile.run("main()")
