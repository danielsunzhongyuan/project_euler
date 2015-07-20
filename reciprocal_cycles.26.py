'''
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:
                1 / 2 = 0.5
                1 / 3 = 0.(3)
                1 / 4 = 0.25
                1 / 5 = 0.2
                1 / 6 = 0.1(6)
                1 / 7 = 0.(142857)
                1 / 8 = 0.125
                1 / 9 = 0.(1)
                1 / 10 = 0.1
Where 0.1(6) means 0.16666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
'''

import math
import time

def is_Prime(n):
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


def main():
    start = time.time()
    primes = [2]
    for i in range(3, 1001):
        if is_Prime(i):
            primes.append(i)
    print primes


    print "It costs:", time.time() - start, "seconds"

if __name__ == "__main__":
    main()
