#! /usr/bin/env python
# encoding: utf-8
import unittest


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def findMin(self, nums):
        if not nums:
            return None
        size = len(nums)
        if size == 1 or nums[0] < nums[size - 1]:
            return nums[0]
        l, r = 0, size - 1
        while l < r:
            mid = (l + r + 1) / 2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid
        return nums[l]


class MinCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_find_min(self):
        s = Solution()
        for arr, ret in [([], None),
                         ([0], 0),
                         ([0, 1], 0),
                         ([1, 0], 0),
                         ([3, 4, 5, 6, 7, 1, 2], 1),
                         ([6, 7, 1, 2, 3, 4, 5], 1)]:
            self.assertEqual(s.findMin(arr), ret)


if __name__ == '__main__':
    unittest.main()
