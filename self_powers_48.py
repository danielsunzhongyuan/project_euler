'''
The series, 1**1 + 2**2 + 3**3 + ... + 10**10 = 10405071317.

Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000**1000.
'''

import math
import time
import profile


def main():
    '''sss'''
    start = time.time()
    print __doc__

    print sum([(i**i)%10**10 for i in range(1, 1001)])%10**10

    print "It costs:", time.time() - start, "seconds"

if __name__ == "__main__":
    profile.run("main()")
