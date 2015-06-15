#! /usr/bin/env python
# encoding: utf-8
import unittest


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        nums.sort()
        count, num = 1, nums[0]
        max, majority = 1, nums[0]
        for i in xrange(1, len(nums)):
            if num == nums[i]:
                count += 1
                if count > max:
                    max = count
                    majority = num
            else:
                count = 1
                num = nums[i]
        return majority



class MajorityElementCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_majority_element(self):
        s = Solution()
        for arr, ret in [([0, 0], 0), ([0, 1, 0], 0),
                         ([0, 1, 2, 3, 2, 2, 2], 2),
                         ([-1, 100, 2, 100, 100, 4, 100], 100)]:
            self.assertEqual(s.majorityElement(arr), ret)


if __name__ == '__main__':
    unittest.main()