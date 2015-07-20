'''
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?


Ten numbers means 10! = 3628800 permutations.
Nine numbers means 9! = 362880 permutations.
'''

import math
import time

def factorial(n):
    if n == 1: return n
    return n * factorial(n-1)

def num_of_chars_needed(lookup, k):
    if k == 0: return 0
    for i in range(1, len(lookup)):
        if lookup[i-1] <= k and k < lookup[i]:
            return i

def kth_lexi(arry, lookup, k):
    arr = [i for i in arry]
    if len(arr) == 1:
        return arr[0]
    if k == 0:
        return ''.join(arr)
    if k < lookup[0] - 1 or lookup[-1] < k + 1:
        return "Error index: %d" % k
    result = ""
    ind = num_of_chars_needed(lookup, k)
    not_used = ''
    for i in range(len(arr) - ind - 1):
        not_used += arr.pop(0)

    divider, reminder = k / lookup[ind-1], k % lookup[ind-1]
    tmp = arr.pop(divider)
    return not_used + tmp + kth_lexi(arr, lookup, reminder)


def main():
    start = time.time()
    arr = [str(i) for i in range(10)]
    lookup = [0] * len(arr)
    for i in range(len(arr)):
        lookup[i] = factorial(i+1)

    print kth_lexi(arr, lookup, 1000000-1)
    print kth_lexi(arr, lookup, 0)
    print kth_lexi(arr, lookup, 1)
    print kth_lexi(arr, lookup, 3628800 - 1)

    print "It costs:", time.time() - start, "seconds"

if __name__ == "__main__":
    main()
