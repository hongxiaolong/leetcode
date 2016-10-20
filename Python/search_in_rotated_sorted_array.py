# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""33. Search in Rotated Sorted Array

Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search.

If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Source : https://leetcode.com/problems/search-in-rotated-sorted-array/
Author : hongxiaolong
Date   : 2016-10-20

"""


import unittest


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1

        if len(nums) == 1:
            return 0 if target == nums[0] else -1

        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) / 2
            if target == nums[m]:
                return m
            if nums[m] < nums[r]:
                if target > nums[m] and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target < nums[m] and target >= nums[l]:
                    r = m - 1
                else:
                    l = m + 1

        return -1


class SearchCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_search(self):
        s = Solution()
        for i, o in [(([], 0), -1),
                     (([1], 1), 0),
                     (([1, 2], 1), 0),
                     (([1, 2], 2), 1),
                     (([1, 2], 0), -1),
                     (([1, 2], 3), -1),
                     (([4, 3], 4), 0),
                     (([4, 3], 3), 1),
                     (([4, 3], 0), -1),
                     (([4, 3], 5), -1),
                     (([5, 6, 8, 9, 0, 1, 4], 6), 1),
                     (([5, 6, 8, 9, 0, 1, 4], 1), 5),
                     (([5, 6, 8, 9, 0, 1, 4], 7), -1),
                     (([5, 6, 8, 9, 0, 1, 4], 3), -1),
                     (([6, 7, 9, 0, 1, 3, 4, 5], 7), 1),
                     (([6, 7, 9, 0, 1, 3, 4, 5], 1), 4),
                     (([6, 7, 9, 0, 1, 3, 4, 5], 8), -1),
                     (([6, 7, 9, 0, 1, 3, 4, 5], 2), -1)]:
            self.assertEqual(s.search(i[0], i[1]), o)


if __name__ == '__main__':
    unittest.main()
