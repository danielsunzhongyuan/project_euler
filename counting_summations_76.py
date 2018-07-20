# -*- coding:utf-8 -*-
'''
Counting summations
Problem 76 
It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?
'''

import profile
import time


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        self.backtrack(res, [], candidates, target, 0)
        return res

    def backtrack(self, res, tmp_res, candidates, remain, start):
        if remain < 0:
            return
        elif remain == 0:
            print tmp_res
            res.append([i for i in tmp_res])
        else:
            i = start
            while i < len(candidates):
                tmp_res.append(candidates[i])
                self.backtrack(res, tmp_res, candidates, remain - candidates[i], i)
                tmp_res.pop()
                i += 1


class Solution2(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        sortedCandidates = sorted(candidates)
        return self.__impl(sortedCandidates, target)

    def __impl(self, sortedCandidatesSub, quota):
        ret = list()
        for i, c in enumerate(sortedCandidatesSub):
            if quota > (c + c):
                tails = self.__impl(sortedCandidatesSub[i:], quota - c)
                ret += [[c] + l for l in tails]
            elif quota == c + c:
                ret.append([c, c])
            elif quota == c:
                ret.append([c])
            elif quota < c:
                break
        return ret

MaxRange = 100


def main():
    start = time.time()
    print __doc__
    print "####### result below #######"

    a = Solution2()
    b = [i for i in range(1, MaxRange)]
    c = a.combinationSum(b, MaxRange)
    print len(c)

    print "####### result done #######"
    print "It costs:", time.time() - start, "seconds"


if __name__ == "__main__":
    profile.run("main()")
