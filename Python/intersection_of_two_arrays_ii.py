# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""350. Intersection of Two Arrays II

Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?


Source : https://leetcode.com/problems/intersection-of-two-arrays-ii/
Author : hongxiaolong
Date   : 2016-10-12

"""


import unittest


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n1, n2 = len(nums1), len(nums2)
        if n1 == 0 or n2 == 0:
            return []

        nums1.sort()
        nums2.sort()

        lst = []
        i, j = 0, 0
        while i < n1 and j < n2:
            if nums1[i] == nums2[j]:
                lst.append(nums1[i])
                i, j = i + 1, j + 1
            elif nums1[i] < nums2[j]:
                i = i + 1
            elif nums1[i] > nums2[j]:
                j = j + 1

        return lst


class IntersectCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_intersect(self):
        s = Solution()
        for i, o in [(([], []), []),
                     (([-1, 0, 1], [2]), []),
                     (([-1, 0, 1, 1, 2, 2], [1, 1, 2]), [1, 1, 2]),
                     (([9, 1, -1, 2, 0, 0], [2, 2, 0, 0, -1]), [-1, 0, 0, 2])]:
            self.assertEqual(s.intersect(i[0], i[1]), o)


if __name__ == '__main__':
    unittest.main()
