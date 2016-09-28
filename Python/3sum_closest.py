# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""16. 3Sum Closest

Given an array S of n integers, find three integers in S
such that the sum is closest to a given number, target.
Return the sum of the three integers.
You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Source : https://leetcode.com/problems/3sum-closest/
Author : hongxiaolong
Date   : 2016-09-28

"""

import sys
import unittest


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        closest = sys.maxint

        for i in xrange(len(nums)):
            l, r = i + 1, len(nums) - 1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if target == sum:
                    closest = sum
                    break
                elif target > sum:
                    l += 1
                else:
                    r -= 1

                if abs(sum - target) < abs(closest - target):
                    closest = sum

        return closest


class ThreeSumClosestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_three_sum_closest(self):
        s = Solution()
        for i, o in [(([-1, 2, 1, -4], 1), 2)]:
            self.assertEqual(s.threeSumClosest(i[0], i[1]), o)
