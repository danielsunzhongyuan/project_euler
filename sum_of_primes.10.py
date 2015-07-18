'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

import math
import time

max_prime = 2000000

def prime_sum(n):
    if n<2: return 0
    if n == 2: return 2
    if n % 2 == 0: n += 1
    primes = [True] * n
    primes[0], primes[1] = [None] * 2
    result = 0
    for i, v in enumerate(primes):
        if v is True and i > n**0.5 + 1:
            result += i
        elif v is True:
            primes[i*2::i] = [False] * (((n-1)//i)-1)
            result += i
    return result

def main():
    global max_prime
    start = time.time()
    print prime_sum(2000000)
    print "Elapsed:", time.time() - start

if __name__ == "__main__":
    main()
