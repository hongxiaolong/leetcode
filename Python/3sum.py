# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""15. 3Sum

Given an array S of n integers, are there elements a, b, c in S
such that a + b + c = 0? Find all unique triplets
in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

Source : https://leetcode.com/problems/3sum/
Author : hongxiaolong
Date   : 2016-10-06

"""


import unittest


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        lst = []
        nums.sort()
        for i in xrange(len(nums)):
            val = 0 - nums[i]
            l, r = i + 1, len(nums) - 1
            while(l < r):
                if (nums[l] + nums[r] == val):
                    three = [nums[i], nums[l], nums[r]]
                    if (three not in lst):
                        lst.append(three)
                    l += 1
                    r -= 1
                elif (nums[l] + nums[r] < val):
                    l += 1
                else:
                    r -= 1

        return lst


class ThreeSumCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_three_sum(self):
        s = Solution()
        for i, o in [([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
                     ([], []),
                     ([-2, 0, 1, 1, 2], [[-2, 0, 2], [-2, 1, 1]])]:
            self.assertEqual(s.threeSum(i), o)


if __name__ == '__main__':
    unittest.main()
