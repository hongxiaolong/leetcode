#!/usr/bin/env python
# encoding: utf-8

"""198. House Robbe

You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that
adjacent houses have security system connected and it
will automatically contact the police if
two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing
the amount of money of each house, determine the maximum amount of
money you can rob tonight without alerting the police.

Source : https://leetcode.com/problems/house-robber/
Author : hongxiaolong
Date   : 2016-08-31

"""

import unittest


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        if n < 2:
            return 0 if n == 0 else nums[0]

        dp = [nums[0], max(nums[0], nums[1])] + [0] * (n - 2)

        for i in xrange(2, n):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[n - 1]


class RobCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_rob(self):
        s = Solution()
        for i, o in [([], 0),
                     ([1], 1),
                     ([1, 2], 2),
                     ([1, 2, 3], 4),
                     ([10, 2, 5, 1, 3], 18),
                     ([10, 1, 1, 29, 5, 100, 5, 6], 145)]:
            self.assertEqual(s.rob(i), o)


if __name__ == '__main__':
    unittest.main()
