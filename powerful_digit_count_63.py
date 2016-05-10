'''
The 5-digit number, 16807=7**5, is also a fifth power. Similarly, the 9-digit number, 134217728=8**9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
'''

import math
import time
import profile


def main():
    '''sss'''
    start = time.time()
    print __doc__

    count = 0
    for i in range(1, 10):
        n = 1
        while True:
            if len(str(i**n)) == n:
                count += 1
                print "%d**%d = %d" % (i, n, i**n)
                n += 1
            else:
                break
    print "count: %d" % count

    print "It costs:", time.time() - start, "seconds"

if __name__ == "__main__":
    profile.run("main()")
