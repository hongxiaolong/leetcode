# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""80. Remove Duplicates from Sorted Array II

Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5,
with the first five elements of nums being 1, 1, 2, 2 and 3.

It doesn't matter what you leave beyond the new length.

Source : https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
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
        if len(nums) < 3:
            return len(nums)

        p, n, d = nums[0], 0, 1
        for i in xrange(1, len(nums)):
            if nums[i] == p:
                d = d + 1 if d < 2 else d
                continue
            else:
                for j in xrange(d):
                    nums[n] = p
                    n += 1
                p = nums[i]
                d = 1

        for j in xrange(d):
            nums[n] = p
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
                     ([0, 0], 2),
                     ([0, 1, 1, 2, 2, 3], 6),
                     ([1, 1, 1, 2, 2, 3], 5)]:
            self.assertEqual(s.removeDuplicates(i), o)


if __name__ == '__main__':
    unittest.main()
