'''
[23, 37, 53, 73, 313, 317, 373, 797, 3137, 3797, 739397]
sum = 739397
'''

import math
import time
import profile

max_prime = 1000000

def get_primes(n):
    if n < 2: return 0
    if n == 2: return 2
    if n % 2 == 0: n += 1

    primes = [True] * n
    primes[0], primes[1] = [None] * 2
    ret = []
    for i, v in enumerate(primes):
        if v and i > n**0.5 + 1:
            ret.append(i)
        elif v:
            primes[i*2::i] = [False] * (((n-1)//i)-1)
            ret.append(i)
    return ret


def get_truncatable_primes(n):
    """
    It costs: 106.038696051 seconds
             235517 function calls in 103.954 seconds
    """
    primes = get_primes(n)
    truncatable_primes = []
    for prime in primes:
        for i in range(1, len(str(prime))):
            if int(str(prime)[0:i]) not in primes or int(str(prime)[i::]) not in primes:
                break
        else:
            truncatable_primes.append(prime)
    return truncatable_primes


def get_truncatable_primes_2():
    right_truncatable_primes = [p for g in get_right_truncatable_primes() for p in g]
    print right_truncatable_primes
    print "There are %d right truncatable primes in total" % len(right_truncatable_primes)
    truncatable_primes = []
    for prime in right_truncatable_primes:
        if is_left_truncatable_prime(prime):
            truncatable_primes.append(prime)
    return truncatable_primes


def get_right_truncatable_primes():
    generation = [[2, 3, 5, 7]]
    while True:
        next_generation = []
        for p in generation[-1]:
            for digit in [1, 3, 7, 9]:
                if is_prime(p*10 + digit):
                    next_generation.append(p*10 + digit)
        if next_generation == []: break
        else: generation.append(next_generation)
    print generation
    print "There are %d right truncatable primes" % sum(len(i) for i in generation)
    return generation[1::]


def is_prime(n):
    if n < 2: return False
    if n == 2 or n == 3: return True
    if n % 2 == 0: return False
    if sum([int(x) for x in str(n)]) % 3 == 0: return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def is_left_truncatable_prime(n):
    return all([is_prime(n%10**i) for i in range(1, len(str(n)))])


def main():
    start = time.time()
    print __doc__

    ######
    print get_truncatable_primes_2()
    ######

    print "It costs:", time.time() - start, "seconds"

if __name__ == "__main__":
    profile.run("main()")
