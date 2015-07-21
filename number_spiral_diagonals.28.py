'''
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.
                    101 = 25 + 21 + 17 + 13 + 9 + 7 + 5 + 3 + 1
What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

Solution:
For n by n spiral (n>1 and n is odd), the four numbers should be:
          n^2, n^2 - (n-1), n^2 - 2*(n-1), n^2 - 3*(n-1)
'''

import math
import time

def sum_of_four_corner(n):
    if n == 1: return 1
    if n < 3 or n%2 == 0:
        return 0
    return 4*n*n - 6*n + 6


def main():
    start = time.time()
    print sum_of_four_corner(1)
    print sum_of_four_corner(3)
    print sum_of_four_corner(5)
    sum = 0
    for i in range(1, 1002, 2):
        sum += sum_of_four_corner(i)
    print sum
    print "It costs:", time.time() - start, "seconds"

if __name__ == "__main__":
    main()
