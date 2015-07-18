'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''
N = 1000

def multiples(n):
    for i in range(n):
        if 0 == i%3 or 0 == i%5:
            yield i

def main():
    print(sum(multiples(N)))


if __name__ == "__main__":
    main()
