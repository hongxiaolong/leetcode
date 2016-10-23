# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""375. Guess Number Higher or Lower II

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong,
I'll tell you whether the number I picked is higher or lower.

However, when you guess a particular number x, and you guess wrong,
you pay $x. You win the game when you guess the number I picked.

Example:

n = 10, I pick 8.

First round:  You guess 5, I tell you that it's higher. You pay $5.
Second round: You guess 7, I tell you that it's higher. You pay $7.
Third round:  You guess 9, I tell you that it's lower. You pay $9.

Game over. 8 is the number I picked.

You end up paying $5 + $7 + $9 = $21.
Given a particular n >= 1,
find out how much money you need to have to guarantee a win.

Source : https://leetcode.com/problems/guess-number-higher-or-lower-ii/
Author : hongxiaolong
Date   : 2016-10-23

"""


import unittest


class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [[0] * (n + 1) for i in xrange(n + 1)]

        def solve(start, end):
            if start < end and dp[start][end] == 0:
                dp[start][end] = min(
                    i + max(solve(start, i - 1), solve(i + 1, end))
                    for i in xrange(start, end))
            return dp[start][end]

        return solve(1, n)


class GuessNumberCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_guess_number(self):
        s = Solution()
        for i, o in [(10, 16)]:
            self.assertEqual(s.getMoneyAmount(i), o)


if __name__ == '__main__':
    unittest.main()
