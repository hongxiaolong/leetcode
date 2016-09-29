# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""213. House Robber II

Note: This is an extension of House Robber.

After robbing those houses on that street,
the thief has found himself a new place for his thievery
so that he will not get too much attention.
This time, all houses at this place are arranged in a circle.
That means the first house is the neighbor of the last one.
Meanwhile, the security system for these houses remain the same
as for those in the previous street.

Given a list of non-negative integers representing the amount of money
of each house, determine the maximum amount of money
you can rob tonight without alerting the police.

Source : https://leetcode.com/problems/house-robber-ii/
Author : hongxiaolong
Date   : 2016-09-29

"""

import unittest


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        if n < 3:
            return 0 if n == 0 else max(nums)

        nl, nr = nums[0:n - 1], nums[1:n]
        dl = [nl[0], max(nl[0], nl[1])]
        dr = [nr[0], max(nr[0], nr[1])]
        for i in xrange(2, n - 1):
            dl.append(max(dl[i - 1], dl[i - 2] + nl[i]))
            dr.append(max(dr[i - 1], dr[i - 2] + nr[i]))

        return max(max(dl), max(dr))


class RobCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_three_sum_closest(self):
        s = Solution()
        for i, o in [([], 0),
                     ([0, 0], 0),
                     ([0, 1, 2, 3], 4),
                     ([0, 1, 2, 3, 4], 6),
                     ([4, 1, 2, 3, 4], 7)]:
            self.assertEqual(s.rob(i), o)
