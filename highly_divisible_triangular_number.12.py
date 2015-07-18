'''
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

   1: 1
   3: 1,3
   6: 1,2,3,6
   10: 1,2,5,10
   15: 1,3,5,15
   21: 1,3,7,21
   28: 1,2,4,7,14,28
   We can see that 28 is the first triangle number to have over five divisors.

   What is the value of the first triangle number to have over five hundred divisors?
'''

import math

def generate_triangle():
    a = 1
    while True:
        yield a*(a+1)/2
        a += 1

def number_of_factors(n):
    max_factor = int(math.sqrt(n) + 1)
    numbers = 0
    for i in range(1, max_factor):
        if n % i == 0:
            numbers += 2
    return numbers
def main():
    a = generate_triangle()
    for i in a:
        if number_of_factors(i) >= 500:
            print i
            break

if __name__ == "__main__":
    main()
