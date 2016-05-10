'''
Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ~ 62%.
8 = count(3, 5, 7, 17, 31, 37, 43)
13 = count(1, 3, 5, 7, 9, 13, 17, 21, 25, 31, 37, 43, 49)

If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?
'''

import math
import time
import profile


def is_prime(n):
    if n < 2: return False
    if n == 2 or n == 3: return True
    for i in xrange(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def main():
    '''sss'''
    start = time.time()
    print __doc__

    odd_squares_count = 1
    prime_count = 0
    spiral_length = 1
    while True:
        spiral_length += 2
        odd_squares_count += 4
        squares = [spiral_length * spiral_length - (spiral_length - 1), spiral_length * spiral_length - (spiral_length - 1) * 2, spiral_length * spiral_length - (spiral_length - 1) * 3]
        for square in squares:
            if is_prime(square):
                prime_count += 1
        ratio = 1.0 * prime_count / odd_squares_count
        if ratio < 0.1:
            print spiral_length, ratio
            break

    print "It costs:", time.time() - start, "seconds"

if __name__ == "__main__":
    profile.run("main()")
