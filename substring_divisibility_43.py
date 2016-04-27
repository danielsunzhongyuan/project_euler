'''
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.
'''

import math
import time
import profile
import itertools


def is_prime(n):
    if n < 2: return False
    if n == 2 or n == 3: return True
    if n % 2 == 0: return False
    if sum([int(c) for c in str(n)]) % 3 == 0: return False

    m = int(math.sqrt(n)) + 1
    for i in range(5, m):
        if n % i == 0:
            return False
    return True


def is_divisible_permutation(aPermutation):
    if aPermutation[0] == 0:
        return False
    #return all(not is_prime(aPermutation[i]*100 + aPermutation[i+1]*10 + aPermutation[i+2]) for i in range(1, 8))
    if aPermutation[3] % 2 == 1:
        return False
    if sum(aPermutation[2:5]) % 3:
        return False
    if aPermutation[5] % 5:
        return False
    if (aPermutation[4]*100 + aPermutation[5]*10 + aPermutation[6]) % 7:
        return False
    if (aPermutation[5]*100 + aPermutation[6]*10 + aPermutation[7]) % 11:
        return False
    if (aPermutation[6]*100 + aPermutation[7]*10 + aPermutation[8]) % 13:
        return False
    if (aPermutation[7]*100 + aPermutation[8]*10 + aPermutation[9]) % 17:
        return False
    return True


def main():
    start = time.time()
    print __doc__

    divisible_permutations = filter(is_divisible_permutation, itertools.permutations(range(0,10), 10))
    numbers = [int(''.join([str(c) for c in divisible_permutations[i]])) for i in range(len(divisible_permutations))]
    print sum(numbers)

    print "It costs:", time.time() - start, "seconds"

if __name__ == "__main__":
    profile.run("main()")
