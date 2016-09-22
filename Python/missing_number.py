#!/usr/bin/env python
# encoding: utf-8

"""268. Missing Number

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n,
find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity.
Could you implement it using only constant extra space complexity?

Source : https://leetcode.com/problems/missing-number/
Author : hongxiaolong
Date   : 2016-08-30

"""

import unittest


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        bitmap = 2 ** (len(nums) + 1) - 1
        for i in nums:
            bitmap = bitmap ^ (2 ** i)

        n = 0
        while True:
            bitmap = bitmap >> 1
            if bitmap == 0:
                break
            n = n + 1

        return n


class MissingNumberCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_missing_number(self):
        s = Solution()
        for i, o in [([0], 1),
                     ([1], 0),
                     ([0, 1, 3], 2),
                     ([0, 2, 3, 4, 7, 6, 5], 1)]:
            self.assertEqual(s.missingNumber(i), o)


if __name__ == '__main__':
    unittest.main()
