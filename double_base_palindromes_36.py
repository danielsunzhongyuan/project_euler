'''
The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
'''

import math
import time
import profile


def isPalindrome(n):
    n_str = str(n)
    return n_str == n_str[::-1]


def main():
    start = time.time()
    print __doc__

    res = 0
    #for i in range(1, 1000000, 2):
    #    if isPalindrome(i) and isPalindrome(bin(i)[2::]):
    #        res += i
    #print res
    print sum([x for x in xrange(1, 1000000, 2) if str(x) == str(x)[::-1] and bin(x)[2::] == bin(x)[-1:1:-1]])
    print "It costs:", time.time() - start, "seconds"

if __name__ == "__main__":
    profile.run("main()")
