# -*- coding:utf-8 -*-
'''
Path sum: two ways
Problem 81 
In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, 
by only moving to the right and down, is indicated in bold red and is equal to 2427.

Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."), 
a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right by only moving right and down.
'''

import profile
import time


def main():
    start = time.time()
    print __doc__
    print "####### result below #######"

    with open("./p081_matrix.txt", "rb") as f:
        a = f.readlines()
    b = [[int(y) for y in x.split(",")] for x in a]

    for i in range(78, -1, -1):
        b[79][i] += b[79][i+1]
        b[i][79] += b[i+1][79]

    for i in range(78, -1, -1):
        for j in range(78, -1, -1):
            b[i][j] += min(b[i+1][j], b[i][j+1])

    print b[0][0]

    print "####### result done #######"
    print "It costs:", time.time() - start, "seconds"


if __name__ == "__main__":
    profile.run("main()")
