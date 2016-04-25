'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
Note: 9! = 362880
'''

import math
import time

def get_factorial(n):
    if n <= 1: return 1
    return n * get_factorial(n-1)

def sum_factorial_digits(number, m):
    result = 0
    while number:
        x = number % 10
        result += m[x]
        number = number / 10
    return result

def main():
    start = time.time()
    fac_map = {}
    results = []
    for i in range(0, 10):
        fac_map[i] = get_factorial(i)
    for number in range(3, get_factorial(9)*7):
        if number == sum_factorial_digits(number, fac_map):
            results.append(number)
    print results
    print "sum of results:", sum(results)
    print "It costs:", time.time() - start, "seconds"

if __name__ == "__main__":
    main()
