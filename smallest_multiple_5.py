'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

import math

N = 20

def divide_factors(n, factors):
    if n == 1:
        return factors
    min_factor = 1
    for i in range(2, n):
        if n % i == 0:
            factors[i] = factors.get(i, 0) + 1
            min_factor = i
            break
    if min_factor == 1:
        factors[n] = factors.get(n, 0) + 1
    else:
        divide_factors(n/min_factor, factors)
    return factors

def main():
    factors = {}
    for i in range(2, N + 1):
        f_i = divide_factors(i, {})
        for k, v in f_i.items():
            if v > factors.get(k, 0):
                factors[k] = v

    result = 1
    for k, v in factors.items():
        result *= math.pow(k, v)
    print "factors:", factors
    print "Result:", int(result)
    return

if __name__ == "__main__":
    main()
