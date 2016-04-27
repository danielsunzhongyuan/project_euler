'''
The nth term of the sequence of triangle numbers is given by, tn = n(n+1)/2; so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
'''

import math
import time
import profile

triangle_numbers = [i*(i+1)/2 for i in range(0, 30)]

def is_triangle_word(word):
    global triangle_numbers
    n = sum([ord(c) - ord('A') + 1 for c in word])
    return n in triangle_numbers

def main():
    start = time.time()
    print __doc__

    with open("p042_words.txt", "rU") as file_handler:
        x = file_handler.read()
        y = x.split(",")
        z = [word.strip("\"") for word in y]

    triangle_words = filter(is_triangle_word, z)
    print len(triangle_words)

    print "It costs:", time.time() - start, "seconds"

if __name__ == "__main__":
    profile.run("main()")
