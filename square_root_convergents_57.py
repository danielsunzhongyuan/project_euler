'''
It is possible to show that the square root of two can be expressed as an infinite continued fraction.

math.sqrt(2) = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator with more digits than denominator?
'''

import math
import time
import profile


def get_numerator_and_denominator(N):
    a, b = 3, 2
    for i in xrange(N):
        yield (a, b)
        a, b = a+2*b, a+b

def main():
    '''sss'''
    start = time.time()
    print __doc__

    ret = 0
    for a, b in  get_numerator_and_denominator(1000):
        if len(str(a)) > len(str(b)):
            ret += 1
    print ret
    print "It costs:", time.time() - start, "seconds"

if __name__ == "__main__":
    profile.run("main()")
