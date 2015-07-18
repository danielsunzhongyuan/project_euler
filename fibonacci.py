N = 4000000
def fibonacci(n):
    a = 1
    b = 2
    while a < n:
        yield a
        a, b = b, a+b

def main():
    a = fibonacci(N)
    sum = 0
    for i in a:
        if i%2 == 0:
            sum += i
    print sum


if __name__ == "__main__":
    main()
