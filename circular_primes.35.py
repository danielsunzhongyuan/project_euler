'''
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?

NOTE:
[2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197, 199, 311, 337, 373, 719, 733, 919, 971, 991, 1193, 1931, 3119, 3779, 7793, 7937, 9311, 9377, 11939, 19391, 19937, 37199, 39119, 71993, 91193, 93719, 93911, 99371, 193939, 199933, 319993, 331999, 391939, 393919, 919393, 933199, 939193, 939391, 993319, 999331]
55 in total
'''

import math
import time
import profile
import unittest


def get_primes_below_n(n):
    result = []
    if n<2: return result
    if n==2: return [2]
    if n%2 == 0: n+=1
    primes = [True] * n
    primes[0], primes[1] = [None] * 2
    for i, v in enumerate(primes):
        if v and i > n**0.5 + 1:
            result.append(i)
        elif v:
            primes[i*2::i] = [False] * (((n-1)//i)-1)
            result.append(i)
    return result

class PrimesTest(unittest.TestCase):
    def setUp(self):
        pass

    def test1(self):
        self.assertEqual(get_primes_below_n(0), [])

    def test2(self):
        self.assertEqual(get_primes_below_n(1), [])

    def test3(self):
        self.assertEqual(get_primes_below_n(2), [2])

    def test4(self):
        self.assertEqual(get_primes_below_n(3), [2,3])

    def test5(self):
        self.assertEqual(get_primes_below_n(11), [2,3,5,7,11])

    def tearDown(self):
        pass

def get_rotations(n):
    if n <= 0: return [0]
    if 1 <= n and n < 10: return [n]
    length = len(str(n))
    result = [n]
    tmp = n
    for i in range(1, length):
        tmp = tmp/10**(length-1) + 10 * (tmp%10**(length-1))
        result.append(tmp)

    return result

def main():
    start = time.time()
    primes = get_primes_below_n(1000000)
    print primes
    rotations = []
    result = []
    for i in primes:
        rotations = get_rotations(i)
        status = True
        for rotation in rotations:
            if rotation not in primes:
                status = False
                break
        if status:
            result.append(i)

    print result
    print "numbers:", len(result)

    print "It costs:", time.time() - start, "seconds"

if __name__ == "__main__":
    #profile.run("unittest.main()")
    profile.run("main()")
