'''
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
'''

import math
import time
import profile


N = 1000000
def main():
    '''sss'''
    start = time.time()
    print __doc__

    primes = [True] * N
    primes[0], primes[1] = False, False
    for i in xrange(2, N/2 + 1):
        if primes[i]:
            tmp = i*2
            while tmp < N:
                primes[tmp] = False
                tmp += i

    allPrimes = [x for x in xrange(N) if primes[x]]
    print allPrimes[-1]
    del primes

    maxN = 0
    maxP = 0
    for i in xrange(len(allPrimes)):
        currentN = 1
        currentP = allPrimes[i]
        if maxP - allPrimes[i] + allPrimes[i+maxN] > allPrimes[-1]:
            break
        for j in range(i+1, len(allPrimes)):
            currentN += 1
            currentP += allPrimes[j]
            if currentP in allPrimes and currentN > maxN:
                maxN = currentN
                maxP = currentP
                print "maxN is %d, maxP is %d, startPrime is %d" % (maxN, maxP, allPrimes[i])
            if currentP > allPrimes[-1]:
                break
    print maxN, maxP, allPrimes[i-1], sum(allPrimes[i-1:i+maxN-1]), allPrimes[i+maxN-2]
    print "It costs:", time.time() - start, "seconds"

if __name__ == "__main__":
    profile.run("main()")
