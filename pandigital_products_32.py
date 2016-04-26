'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 * 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
'''

import math
import time
import profile

def is_pandigital(string):
    if len(string) != 9:
        return False
    if ''.join(sorted(string)) == '123456789':
        return True
    else:
        return False


def main():
    start = time.time()
    total = 0
    string = ''
    results = set([])
    for i in range(2, 10):
        for j in range(1000, 9876):
            if is_pandigital(str(i) + str(j) + str(i*j)):
                print i, "*", j, "=", i*j
                total += i*j
                results.add(i*j)
    for i in range(10, 100):
        for j in range(100, 987):
            if is_pandigital(str(i) + str(j) + str(i*j)):
                print i, "*", j, "=", i*j
                total += i*j
                results.add(i*j)

    print "total:", total
    print "results:", sum(results)

    print "It costs:", time.time() - start, "seconds"

if __name__ == "__main__":
    profile.run("main()")
