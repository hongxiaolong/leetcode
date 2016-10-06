#!/usr/bin/env python
# encoding: utf-8

"""172. Factorial Trailing Zeroes

Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.

Source : https://leetcode.com/problems/factorial-trailing-zeroes/
Author : hongxiaolong
Date   : 2016-10-06

"""

import unittest


class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        x = 5
        num = 0
        while n >= x:
            num += n / x
            x *= 5
        return num


class TrailingZeroesCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_trailing(self):
        s = Solution()
        for a, b in [(0, 0),
                     (1, 0),
                     (10, 2),
                     (123456, 30860)]:
            self.assertEqual(s.trailingZeroes(a), b)


if __name__ == '__main__':
    unittest.main()
