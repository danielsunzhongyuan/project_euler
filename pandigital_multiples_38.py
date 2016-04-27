'''
Take the number 192 and multiply it by each of 1, 2, and 3:

192 * 1 = 192
192 * 2 = 384
192 * 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
'''

import math
import time
import profile


def is_concatenated_product(string):
    return "0" not in str(string) and 9 == len(str(string)) and 9 == len(set([c for c in str(string)]))


def main():
    start = time.time()
    print __doc__

    # the integer can't be larger than 9999, because n >= 2
    print "###############"
    for i in range(4, 0, -1):
        for j in xrange(10**i-1, 10**(i-1)-1, -1):
            string = ""
            for k in range(1, 9 / i + 1):
                string += str(j*k)
            if is_concatenated_product(string):
                print string, j

    print "It costs:", time.time() - start, "seconds"
    print "###############"

if __name__ == "__main__":
    profile.run("main()")
