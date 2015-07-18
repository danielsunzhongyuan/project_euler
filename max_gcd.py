'''
Two ways to get the GCD of two numbers.
The first one is normal way, while the second one works better for really big numbers
'''

import math
import time

def gcd_1(a, b):
    if b == 0: return a
    return gcd_1(b, a % b)

def gcd_2(a, b):
    if a < b:
        a, b = b, a
    if b == 0: return a

    if a%2 == 0 and b%2 == 0:
        return 2 * gcd_2(a/2, b/2)
    if a%2 == 0:
        return gcd_2(a/2, b)
    if b%2 == 0:
        return gcd_2(a, b/2)

    return gcd_2((a+b)/2, (a-b)/2)

def main():
    start = time.time()
    x, y = 23428374212489279834729837492873823658346578364141098429384837482374927983472, 28237482636587238490892379823578298324729837418274982784927984192239798247298374182749827849279841922
    print "length of x, y are:", len(str(x)), len(str(y))
    gcd = gcd_1(x, y)
    mid = time.time()
    print "method1 costs %f seconds to get %d." % (mid-start, gcd)
    gcd = gcd_2(x, y)
    print "method2 costs %f seconds to get %d." % (time.time() - mid, gcd)

if __name__ == "__main__":
    main()
