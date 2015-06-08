#!/usr/bin/env python
# encoding: utf-8
import unittest


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        ret = 0
        for i in nums:
            ret = ret ^ i
        return ret


class SingleNumberCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_single_number(self):
        s = Solution()
        for nums, rets in [([0, 1, 1], 0), ([0, 2, 10, 10, 0], 2)]:
            self.assertEqual(s.singleNumber(nums), rets)


if __name__ == '__main__':
    unittest.main()
