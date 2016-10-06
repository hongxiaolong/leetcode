#!/usr/bin/env python
# encoding: utf-8

"""34. Search for a Range

Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].

Source : https://leetcode.com/problems/search-for-a-range/
Author : hongxiaolong
Date   : 2016-10-06

"""

import unittest


class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def searchRange(self, nums, target):
        if not nums:
            return [-1, -1]
        size = len(nums)

        # Find the start position.
        l, r = 0, size - 1
        while l + 1 < r:
            mid = l + (r - l) / 2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid

        # Target does not exist in nums.
        if nums[l] != target and nums[r] != target:
            return [-1, -1]
        start = l if nums[l] == target else r

        # Find the end position.
        l, r = 0, size - 1
        while l + 1 < r:
            mid = l + (r - l) / 2
            if nums[mid] <= target:
                l = mid
            else:
                r = mid
        end = r if nums[r] == target else l

        return [start, end]


class SearchCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_search(self):
        s = Solution()
        for arr, tar, ret in [([], 0, [-1, -1]),
                              ([0], 0, [0, 0]),
                              ([0, 0, 0, 1], 0, [0, 2]),
                              ([-1, 0, 0, 0], 0, [1, 3]),
                              ([-1, 0, 1, 2, 2, 2, 3], 2, [3, 5])]:
            self.assertEqual(s.searchRange(arr, tar), ret)


if __name__ == '__main__':
    unittest.main()
