#!/usr/bin/env python
# encoding: utf-8
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
