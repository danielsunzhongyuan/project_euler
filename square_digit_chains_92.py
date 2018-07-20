# -*- coding:utf-8 -*-
'''
Square digit chains
Problem 92 
A number chain is created by continuously adding the square of the digits in a number 
to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop.
What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
'''

import profile
import time

SquareMap = {
    "0": 0, "1": 1, "2": 4,
    "3": 9, "4": 16, "5": 25,
    "6": 36, "7": 49, "8": 64,
    "9": 81
}

MaxRange = 10000000  # 8581146


def get_next(n):
    res = 0
    for i in str(n):
        res += SquareMap[i]
    return res


def main():
    start = time.time()
    print __doc__
    print "####### result below #######"

    a = [-1] * MaxRange
    a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7], a[8], a[9] = 0, 0, 1, 1, 1, 1, 1, 0, 1, 1
    a[10], a[11], a[12], a[13], a[14], a[15], a[16], a[17], a[18], a[19] = 0, 1, 1, 0, 1, 1, 1, 1, 1, 0

    for i in xrange(20, MaxRange):
        if a[i] == -1:
            tmp = [i]
            next_number = get_next(i)
            while next_number > i:
                tmp.append(next_number)
                next_number = get_next(next_number)
            a[i] = a[next_number]
    print sum(a)

    print "####### result done #######"
    print "It costs:", time.time() - start, "seconds"


if __name__ == "__main__":
    profile.run("main()")
