'''
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p <= 1000, is the number of solutions maximised?
'''

import math
import time
import profile


def get_abc(n):
    ret = []
    for a in range(1, n/2):
        for b in range(a+1, (n-a)/2):
            c = n - a - b
            if a**2 + b**2 == c**2:
                ret.append([a, b, c])
    return ret


def main():
    start = time.time()
    print __doc__

    max_length = 3
    for i in xrange(3, 1001):
        abc_groups = get_abc(i)
        length = len(abc_groups)
        if max_length < length:
            max_length = length
            print i
            print abc_groups


    print "It costs:", time.time() - start, "seconds"

if __name__ == "__main__":
    profile.run("main()")
