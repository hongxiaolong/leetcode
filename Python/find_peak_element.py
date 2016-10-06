#!/usr/bin/env python
# encoding: utf-8

"""162. Find Peak Element

A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1],
find a peak element and return its index.

The array may contain multiple peaks,
in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1],
3 is a peak element and your function should return the index number 2.

click to show spoilers.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.

Source : https://leetcode.com/problems/find-peak-element/
Author : hongxiaolong
Date   : 2016-10-06

"""

import unittest


class Solution:
    # @param nums, an integer[]
    # @return an integer
    def findPeakElement(self, nums):
        if not nums:
            return
        n = len(nums)
        for i in xrange(1, n - 1):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                return i

        # return the bigger one if n <= 2
        return [0, n - 1][nums[0] < nums[n - 1]]


class PeakCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_peak(self):
        s = Solution()
        for lst, ret in [([1, 2, 3, 1], 2),
                         ([-10, 4, 6, -10], 2),
                         ([1, 2, 4, 1, 3, 1], 2),
                         ([-10, 0, 5, 4, 6, -10], 2)]:
            self.assertEqual(s.findPeakElement(lst), ret)

        for lst in [[], [1], [1, 0]]:
            self.assertFalse(s.findPeakElement(lst))


if __name__ == '__main__':
    unittest.main()
