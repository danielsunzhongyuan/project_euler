# -*- coding:utf-8 -*-
'''
Digit factorial chains
Problem 74 
The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:

1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; it turns out that there are only three such loops that exist:

169 → 363601 → 1454 → 169
871 → 45361 → 871
872 → 45362 → 872

It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,

69 → 363600 → 1454 → 169 → 363601 (→ 1454)
78 → 45360 → 871 → 45361 (→ 871)
540 → 145 (→ 145)

Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting number below one million is sixty terms.

How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?
'''

import profile
import time

MaxRange = 1000000

FactorialMap = {
    "0": 1, "1": 1, "2": 2,
    "3": 6, "4": 24, "5": 120,
    "6": 720, "7": 5040, "8": 40320,
    "9": 362880
}


def get_next(n):
    res = 0
    for c in str(n):
        res += FactorialMap[c]
    return res


def main():
    start = time.time()
    print __doc__
    print "######## result #########"

    res = []
    a = [[] for _ in range(MaxRange)]
    for i in xrange(1, MaxRange):
        tmp = [i]
        next = get_next(i)
        while next > i and next not in tmp:
            tmp.append(next)
            next = get_next(next)
        if next >= i:
            a[i] = tmp
        else:
            a[i] = list(set(a[next] + tmp))
        if len(a[i]) == 60:
            res.append(i)

    print len(res), res
    print "######## result #########"
    print "It costs:", time.time() - start, "seconds"


if __name__ == "__main__":
    profile.run("main()")
