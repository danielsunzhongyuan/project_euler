'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99
Find the largest palindrome made from the product of two 3-digit numbers
'''
import math
MAX_DIGITALS = 3

def isPalindrome(n):
    n_str = str(n)
    return n_str == n_str[::-1]

def main():
    min = math.pow(10, MAX_DIGITALS-1)
    max = math.pow(10, MAX_DIGITALS)
    min = int(min)
    max = int(max)
    result = 0
    for i in range(min, max):
        for j in range(i, max):
            tmp = i * j
            if isPalindrome(tmp):
                #print tmp, "=", i, "*", j
                result = tmp if result< tmp else result
    print "Max result:", result
    print isPalindrome(9009)
    return

if __name__ == "__main__":
    main()
