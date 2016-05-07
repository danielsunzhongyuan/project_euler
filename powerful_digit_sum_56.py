'''
A googol (10**100) is a massive number: one followed by one-hundred zeros; 100**100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a**b, where a, b < 100, what is the maximum digital sum?
'''

import math
import time
import profile


def main():
    '''sss'''
    start = time.time()
    print __doc__

    maxSum = 0
    for i in xrange(80, 100):
        for j in xrange(80, 100):
            digitSum = sum(int(c) for c in str(i**j))
            if digitSum > maxSum:
                maxSum = digitSum
                print maxSum, i, j

    print "It costs:", time.time() - start, "seconds"

if __name__ == "__main__":
    profile.run("main()")
