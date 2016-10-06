#!/usr/bin/env python
# encoding: utf-8

"""217. Contains Duplicate

Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice
in the array, and it should return false if every element is distinct.

Source : https://leetcode.com/problems/contains-duplicate/
Author : hongxiaolong
Date   : 2016-10-06

"""

import unittest


class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        if len(nums) < 2:
            return False
        nums.sort()
        duplicate = nums[0]
        for i in xrange(1, len(nums)):
            if nums[i] == duplicate:
                return True
            duplicate = nums[i]
        return False


class DuplicateCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_contains_duplicate(self):
        s = Solution()
        for arr, ret in [([], False),
                         ([0], False),
                         ([0, 1], False),
                         ([0, 3, -5, 3], True)]:
            self.assertEqual(s.containsDuplicate(arr), ret)


if __name__ == '__main__':
    unittest.main()
