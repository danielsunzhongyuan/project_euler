'''
n! = n*(n-1)*(n-2)*...*3*2*1
For example, 10! = 10*9*8*...*3*2*1 = 3628800
and sum of the digits in the number is 3+6+2+8+8+0+0=27.

Find the sum of the digits in the number 100!
'''

import math
import time

def fac(n):
    if n == 1:
        return 1
    return n * fac(n-1)

def main():
    start = time.time()
    print sum([int(i) for i in str(fac(100))])
    print "It costs:", time.time() - start, "seconds"

if __name__ == "__main__":
    main()
