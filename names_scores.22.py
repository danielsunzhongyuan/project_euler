'''
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 * 53 = 49714.

What is the total of all the name scores in the file?
'''

import math
import time

def worth(word):
    result = 0
    for i in word:
        result += ord(i) - ord('A') + 1
    return result

def main():
    start = time.time()
    with open("p022_names.txt", 'r') as file_handle:
        a = file_handle.readline()
    names = [i.strip("\"") for i in a.split(',')]
    names = sorted(names)
    print names[-1]
    print names[:10]
    print names[938]
    print names[937]
    print worth(names[0])
    print len(names)
    result = 0
    for i in range(len(names)):
        result += worth(names[i]) * (i+1)
    print result
    print "It costs:", time.time() - start, "seconds"

if __name__ == "__main__":
    main()
