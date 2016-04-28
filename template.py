'''

'''

import math
import time
import profile


def main():
    '''sss'''
    start = time.time()
    print __doc__, math.sqrt(25)

    print "It costs:", time.time() - start, "seconds"

if __name__ == "__main__":
    profile.run("main()")
