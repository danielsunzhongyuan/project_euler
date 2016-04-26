'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
Note: 6, 28, 496, 8128 are not amicable numbers, b/c the sum_of_divisors of the these numbers are themselves.
'''

import math
import time

def sum_of_divisors(n):
    s = 0
    for i in range(1,n/2+1):
        if n%i==0:
            s += i
    return s

def main():
    start = time.time()
    s = 0
    dn = [sum_of_divisors(i) for i in range(1, 10000+1)]
    for i in range(10000):
        if i < dn[i] - 1 and 1<= dn[i] and dn[i] <= 10000 and dn[dn[i]-1] == i+1:
            print i+1, dn[i]
            s += i + 1 + dn[i]
    print s
    print "It costs:", time.time() - start, "seconds"

if __name__ == "__main__":
    main()
