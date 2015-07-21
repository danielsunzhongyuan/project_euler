
'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
import math
N = 600851475143
#N = 13195
def isPrime(n):
    if n < 2: return False
    if n == 2 or n == 3: return True
    sqrt_n = int(math.sqrt(n)) + 1
    for i in range(2, sqrt_n):
        if n % i == 0:
            return False
    return True

def main():
    sqrt_N = int(math.sqrt(N)) + 1
    max_prime_factor = 0
    for i in range(2, sqrt_N):
        if N % i == 0 and isPrime(i):
            max_prime_factor = i
            print i
    print "max_prime_factor:", max_prime_factor

if __name__ == "__main__":
    main()

