#!/usr/bin/env python
# encoding: utf-8

"""300. Longest Increasing Subsequence

Given an unsorted array of integers,
find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101],
therefore the length is 4.
Note that there may be more than one LIS combination,
it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?

Source : https://leetcode.com/problems/longest-increasing-subsequence/
Author : hongxiaolong
Date   : 2016-08-19

"""

import unittest


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [1] * len(nums)
        for i in xrange(len(nums)):
            for j in xrange(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp) if dp else 0


class LongestIncreasingSubsequenceCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_lis(self):
        s = Solution()
        for i, o in [([], 0),
                     ([0], 1),
                     ([10, 9, 2, 5, 3, 7, 101, 18], 4)]:
            self.assertEqual(s.lengthOfLIS(i), o)


if __name__ == '__main__':
    unittest.main()
