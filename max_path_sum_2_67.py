'''
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
                  3
                 7 4
                2 4 6
               8 5 9 3
That is, 3 + 7 + 4 + 9 = 23
Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.
...

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)
'''

import math
import time


def main():
    start = time.time()
    triangle_numbers = []
    with open("triangle_67.txt", 'r') as file_handle:
        for i in file_handle.readlines():
            triangle_numbers.append([int(j) for j in i.split(" ")])
    x = len(triangle_numbers)
    for i in range(x - 2, -1, -1):
        for j in range(0, i + 1):
            triangle_numbers[i][j] += max(triangle_numbers[i+1][j], triangle_numbers[i+1][j+1])
    print triangle_numbers[0][0]
    print "It costs:", time.time() - start, "seconds"

if __name__ == "__main__":
    main()
