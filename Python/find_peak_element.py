#!/usr/bin/env python
# encoding: utf-8
import unittest


class Solution:
    # @param nums, an integer[]
    # @return an integer
    def findPeakElement(self, nums):
        if not nums:
            return
        n = len(nums)
        for i in xrange(1, n - 1):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                return i

        # return the bigger one if n <= 2
        return [0, n - 1][nums[0] < nums[n - 1]]


class PeakCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_peak(self):
        s = Solution()
        for lst, ret in [([1, 2, 3, 1], 2),
                         ([-10, 4, 6, -10], 2),
                         ([1, 2, 4, 1, 3, 1], 2),
                         ([-10, 0, 5, 4, 6, -10], 2)]:
            self.assertEqual(s.findPeakElement(lst), ret)

        for lst in [[], [1], [1, 0]]:
            self.assertFalse(s.findPeakElement(lst))


if __name__ == '__main__':
    unittest.main()
