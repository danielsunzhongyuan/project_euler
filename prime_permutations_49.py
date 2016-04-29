'''
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
'''

import math
import time
import profile


def is_prime(n):
    if n < 2: return False
    if n == 2: return True
    square = int(math.sqrt(n))
    for i in xrange(2, square + 1):
        if n % i == 0:
            return False
    return True


def main():
    '''sss'''
    start = time.time()
    print __doc__

    primes = []
    for i in range(1001, 10000, 2):
        if is_prime(i):
            primes.append(i)

    count = {}
    for prime in primes:
        sorted_prime = "".join(sorted(str(prime)))
        tmp = count.get(sorted_prime, [])
        tmp.append(prime)
        count[sorted_prime] = tmp

    for k, v in count.items():
        for i in range(0, len(v)):
            for j in range(i+1, len(v)):
                if (v[i] + v[j])/2 in v:
                    print k, v



    print "It costs:", time.time() - start, "seconds"

if __name__ == "__main__":
    profile.run("main()")
