'''
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''

import math
import time

def sum_of_divisors(n):
    if n <= 3:
        return 1
    result = 1
    for i in range(2, n/2+1):
        if n%i == 0:
            result += i
    return result


def main():
    start = time.time()
    abundant_nums = []
    for i in range(12, 28124):
        if sum_of_divisors(i) > i:
            abundant_nums.append(i)
    print len(abundant_nums)
    abundant_sums = []
    for i in abundant_nums:
        for j in abundant_nums:
            if i+j < 28124:
                abundant_sums.append(i+j)
    abundant_sums = set(abundant_sums)
    print (1+28123)*28123/2 - sum(abundant_sums)

    print "It costs:", time.time() - start, "seconds"

if __name__ == "__main__":
    main()
