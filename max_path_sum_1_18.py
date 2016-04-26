'''
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
                  3
                 7 4
                2 4 6
               8 5 9 3
That is, 3 + 7 + 4 + 9 = 23
Find the maximum total from top to bottem of the triangle below:
...

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)
'''

import math
import time


def main():
    start = time.time()
    triangle_numbers = []
    triangle_numbers.append([int(i) for i in "75".split(" ")])
    triangle_numbers.append([int(i) for i in "95 64".split(" ")])
    triangle_numbers.append([int(i) for i in "17 47 82".split(" ")])
    triangle_numbers.append([int(i) for i in "18 35 87 10".split(" ")])
    triangle_numbers.append([int(i) for i in "20 04 82 47 65".split(" ")])
    triangle_numbers.append([int(i) for i in "19 01 23 75 03 34".split(" ")])
    triangle_numbers.append([int(i) for i in "88 02 77 73 07 63 67".split(" ")])
    triangle_numbers.append([int(i) for i in "99 65 04 28 06 16 70 92".split(" ")])
    triangle_numbers.append([int(i) for i in "41 41 26 56 83 40 80 70 33".split(" ")])
    triangle_numbers.append([int(i) for i in "41 48 72 33 47 32 37 16 94 29".split(" ")])
    triangle_numbers.append([int(i) for i in "53 71 44 65 25 43 91 52 97 51 14".split(" ")])
    triangle_numbers.append([int(i) for i in "70 11 33 28 77 73 17 78 39 68 17 57".split(" ")])
    triangle_numbers.append([int(i) for i in "91 71 52 38 17 14 91 43 58 50 27 29 48".split(" ")])
    triangle_numbers.append([int(i) for i in "63 66 04 68 89 53 67 30 73 16 69 87 40 31".split(" ")])
    triangle_numbers.append([int(i) for i in "04 62 98 27 23 09 70 98 73 93 38 53 60 04 23".split(" ")])

    x = len(triangle_numbers)
    for i in range(x - 2, -1, -1):
        for j in range(0, i + 1):
            triangle_numbers[i][j] += max(triangle_numbers[i+1][j], triangle_numbers[i+1][j+1])
    print triangle_numbers[0][0]
    print "It costs:", time.time() - start, "seconds"

if __name__ == "__main__":
    main()
