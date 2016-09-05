#!/usr/bin/env python
# encoding: utf-8

"""70. Climbing Stairs

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?

Source : https://leetcode.com/problems/climbing-stairs/
Author : hongxiaolong
Date   : 2016-09-05

"""

import unittest


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return n

        dp = [1, 2]
        for i in xrange(n - 2):
            dp.append(dp[-1] + dp[-2])

        return dp[-1]


class CoinChangeCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_coin_change(self):
        s = Solution()
        for i, o in [(0, 0),
                     (1, 1),
                     (2, 2),
                     (3, 3)]:
            self.assertEqual(s.climbStairs(i), o)


if __name__ == '__main__':
    unittest.main()
