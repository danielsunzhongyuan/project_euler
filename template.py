# -*- coding:utf-8 -*-
'''

'''

import profile
import time


def main():
    start = time.time()
    print __doc__
    print "####### result below #######"

    print "####### result done #######"
    print "It costs:", time.time() - start, "seconds"


if __name__ == "__main__":
    profile.run("main()")
