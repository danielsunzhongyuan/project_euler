'''
The following iterative sequence is defined for the set of positive integers:
          n -> n/2 (n is even)
          n -> 3n + 1 (n is odd)
Using the rule above and starting with 13, we generate the following sequence:
          13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?
'''

import math
import time

def term(x, length=0):  # it uses about 41 seconds
    if x == 1:
        length += 1
        return length
    if x % 2 == 0:
        length += 1
        return term(x/2, length)
    else:
        length += 1
        return term(3*x + 1, length)

def collatz(x):   # it uses about 24 seconds
    count = 1
    while x>1:
        count += 1
        if x % 2 == 0:
            x /= 2
        else:
            x = x * 3 + 1
    return count

def main():
    print collatz(13)
    start = time.time()
    max_chain = [0, 0]
    for i in range(10, 1000000):
        tmp = collatz(i)
        if tmp > max_chain[1]:
            max_chain = [i, tmp]

    print max_chain
    print "It costs:", time.time() - start, "seconds."


if __name__ == "__main__":
    main()
