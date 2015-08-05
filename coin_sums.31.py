'''
In England the currency is made up of pound, L, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, L1 (100p) and L2 (200p).
It is possible to make L2 in the following way:

1*L1 + 1*50p + 2*20p + 1*5p + 1*2p + 3*1p
How many different ways can L2 be made using any number of coins?
'''

import math
import time

def main():
    start = time.time()
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    money = 200
    ways = [0] * (money + 1)
    ways[0] = 1
    for i in coins:
        for j in range(i, money+1):
            ways[j] += ways[j - i]
    print ways



    print "It costs:", time.time() - start, "seconds"

if __name__ == "__main__":
    main()
