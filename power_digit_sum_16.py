'''
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
'''

import math
import time


def main():
    start = time.time()
    x = math.pow(2, 1000)
    b = str(int(x))
    result = 0
    for i in range(len(b)):
        result += int(b[i])
    print result

    y = 2**1000
    yy = str(y)
    result = 0
    for i in range(len(yy)):
        result += int(yy[i])
    print result

    print "It costs:", time.time() - start, "seconds"

if __name__ == "__main__":
    main()
