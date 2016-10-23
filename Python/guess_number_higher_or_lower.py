# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""374. Guess Number Higher or Lower

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong,
I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num)
which returns 3 possible results (-1, 1, or 0):

-1 : My number is lower
 1 : My number is higher
 0 : Congrats! You got it!
Example:
n = 10, I pick 6.

Return 6.

Source : https://leetcode.com/problems/guess-number-higher-or-lower/
Author : hongxiaolong
Date   : 2016-10-23

"""


import unittest


_n = 0


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower,
# 1 if my number is higher, otherwise return 0
def guess(num):

    global _n

    if num > _n:
        return -1
    elif num < _n:
        return 1

    return 0


class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if 0 == guess(n):
            return n

        left, right = 1, n
        while left < right:
            mid = left + (right - left) / 2
            f = guess(mid)
            if 1 == f:
                left = mid
            elif -1 == f:
                right = mid
            else:
                return mid
        return left


class GuessNumberCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_guess_number(self):
        s = Solution()
        for i, o in [((10, 1), 1),
                     ((10, 3), 3),
                     ((10, 5), 5),
                     ((10, 6), 6),
                     ((10, 10), 10),
                     ((1, 1), 1),
                     ((2, 1), 1),
                     ((2, 2), 2)]:
            global _n
            _n = i[1]
            self.assertEqual(s.guessNumber(i[0]), o)


if __name__ == '__main__':
    unittest.main()
