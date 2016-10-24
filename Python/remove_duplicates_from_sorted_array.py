# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""26. Remove Duplicates from Sorted Array

Given a sorted array, remove the duplicates in place
such that each element appear only once and return the new length.

Do not allocate extra space for another array,
you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2,
with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the new length.

Source : https://leetcode.com/problems/remove-duplicates-from-sorted-array/
Author : hongxiaolong
Date   : 2016-10-24

"""


import unittest


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        if len(nums) == 1:
            return 1

        p, n = nums[0], 1
        for i in xrange(1, len(nums)):
            if nums[i] == p:
                continue
            else:
                p = nums[i]
                nums[n] = nums[i]
                n += 1

        return n


class RemoveDuplicatesCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_remove_duplicates(self):
        s = Solution()
        for i, o in [([], 0),
                     ([0], 1),
                     ([0, 0], 1),
                     ([0, 1, 1, 2, 2, 3], 3)]:
            self.assertEqual(s.removeDuplicates(i), o)


if __name__ == '__main__':
    unittest.main()
