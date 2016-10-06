#!/usr/bin/env python
# encoding: utf-8

"""343. Integer Break

Given a positive integer n, break it into the sum of at least
two positive integers and maximize the product of those integers.
Return the maximum product you can get.

For example,
given n = 2, return 1 (2 = 1 + 1);
given n = 10, return 36 (10 = 3 + 3 + 4).

Note: You may assume that n is not less than 2 and not larger than 58.

Source : https://leetcode.com/problems/integer-break/
Author : hongxiaolong
Date   : 2016-10-06

"""

import unittest


class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2 or n == 3:
            return n - 1
        r = 1
        while(n > 4):
            r *= 3
            n -= 3
        return r * n


class IntegerBreakCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_integer_break(self):
        s = Solution()
        for n, r in [(2, 1), (10, 36), (8, 18), (58, 1549681956)]:
            self.assertEqual(s.integerBreak(n), r)


if __name__ == '__main__':
    unittest.main()
