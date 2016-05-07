'''
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
'''

import math
import time
import profile


def main():
    '''sss'''
    start = time.time()
    print __doc__

    print int(1.0 / 7 * 1000000)
    print int(2.0 / 7 * 1000000)
    print int(3.0 / 7 * 1000000)
    print int(4.0 / 7 * 1000000)
    print int(5.0 / 7 * 1000000)
    print int(6.0 / 7 * 1000000)

    print "It costs:", time.time() - start, "seconds"

if __name__ == "__main__":
    profile.run("main()")
