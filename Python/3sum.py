#!/usr/bin/env python
# encoding: utf-8
import unittest


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        lst = []
        nums.sort()
        for i in xrange(len(nums)):
            val = 0 - nums[i]
            l, r = i + 1, len(nums) - 1
            while(l < r):
                if (nums[l] + nums[r] == val):
                    three = [nums[i], nums[l], nums[r]]
                    if (three not in lst):
                        lst.append(three)
                    l += 1
                    r -= 1
                elif (nums[l] + nums[r] < val):
                    l += 1
                else:
                    r -= 1

        return lst


class ThreeSumCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_three_sum(self):
        s = Solution()
        for a, b in [([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
                     ([], []),
                     ([-2, 0, 1, 1, 2], [[-2, 0, 2], [-2, 1, 1]])]:
            self.assertEqual(s.threeSum(a), b)


if __name__ == '__main__':
    unittest.main()
