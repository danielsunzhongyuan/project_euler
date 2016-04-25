'''

'''

import math
import time
import profile


def main():
    start = time.time()
    print __doc__

    print "It costs:", time.time() - start, "seconds"

if __name__ == "__main__":
    profile.run("main()")
