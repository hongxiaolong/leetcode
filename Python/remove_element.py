#!/usr/bin/env python
# encoding: utf-8

"""27. Remove Element

Given an array and a value, remove all instances of that value in place and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:
Given input array nums = [3,2,2,3], val = 3

Your function should return length = 2, with the first two elements of nums being 2.

Source : https://leetcode.com/problems/remove-element/
Author : hongxiaolong
Date   : 2016-10-06

"""

import unittest


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        l, r = len(nums), 0
        for i in xrange(l - 1, -1, -1):
            if nums[i] == val:
                del nums[i]
                r += 1
        return l - r


class RemoveElementCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_remove_element(self):
        s = Solution()
        for arr_bef, v, arr_aft, l in [
            ([3, 2, 2, 3], 3, [2, 2], 2),
            ([], 3, [], 0),
                ([3], 2, [3], 1)]:
            self.assertEqual(s.removeElement(arr_bef, v), l)
            self.assertListEqual(arr_bef, arr_aft)


if __name__ == '__main__':
    unittest.main()
