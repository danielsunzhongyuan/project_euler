'''
Starting in the top left corner of a 2*2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20*20 grid?
'''

import math
import time


def lattic(m, n): # very bad algorithm, it costs 43 seconds for 16*16
    if m == 1:
        return n + 1
    if n == 1:
        return m + 1
    return lattic(m - 1, n) + lattic(m, n - 1)

def lattic_2(m, n):
    x = max(m, n) + 1
    result = [1] * x
    result = [[1] * x for i in result]
    for i in result:
        print i
    for i in range(1, x):
        for j in range(1,i):
            result[i][j] = result[i][j-1] + result[i-1][j]
            result[j][i] = result[i][j]
        result[i][i] = 2 * result[i][i-1]
    for i in result:
        print i
    return result[m][n]
def main():
    start = time.time()
    print lattic_2(20, 20)

    print "It costs:", time.time() - start, "seconds"

if __name__ == "__main__":
    main()
