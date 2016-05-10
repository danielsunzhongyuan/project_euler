'''
The cube, 41063625 (345**3), can be permuted to produce two other cubes: 56623104 (384**3) and 66430125 (405**3). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
'''

import math
import time
import profile


def main():
    '''sss'''
    start = time.time()
    print __doc__
    permutations = {}
    n = 400
    while True:
        cube = n ** 3
        cube_str = str(cube)
        sorted_cube_str = "".join(sorted(cube_str))
        permutations[sorted_cube_str] = permutations.get(sorted_cube_str, 0) + 1
        if permutations[sorted_cube_str] == 5:
            print n, cube, sorted_cube_str
            break
        n += 1
    
    for i in xrange(400, n+1):
        if "".join(sorted(str(i**3))) == sorted_cube_str:
            print i, i**3

    print "It costs:", time.time() - start, "seconds"

if __name__ == "__main__":
    profile.run("main()")
