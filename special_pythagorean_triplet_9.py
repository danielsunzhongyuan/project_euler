'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
                                        a^2 + b^2 = c^2
For example, (3,4,5)
There exists exactly one Pythagorean triplet for which a + b + c = 1000.

Find the product abc.
'''

import math


def main():
    for i in range(1, 334):
        for j in range(i, 500):
            k = 1000 - i - j
            if i*i + j*j == k*k:
                print i,j,k
                print i*j*k
                break

if __name__ == "__main__":
    main()
