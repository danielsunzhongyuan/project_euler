'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
'''

import math

N = 10001

def isPrime(n, primes):
    for i in primes:
        if n % i == 0:
            return False
    return True

    
def main():
    primes = []
    max_prime = int(N*math.log(N)*1.17)
    print max_prime
    for i in range(2, max_prime):
        if isPrime(i, primes):
            primes.append(i)
    #print primes, len(primes), N
    print primes[N-1]

if __name__ == "__main__":
    main()
