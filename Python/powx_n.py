# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""50. Pow(x, n)

Implement pow(x, n).

Source : https://leetcode.com/problems/powx-n/
Author : hongxiaolong
Date   : 2016-10-07

"""


import unittest


class Solution(object):
    def pow(self, x, n):
        if n == 0:
            return 1

        mid = self.pow(x, n / 2)

        if n % 2 == 1:
            return mid * mid * x

        return mid * mid

    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x == 1.0 or n == 0:
            return 1.00000

        sp = self.pow(x, abs(n))
        sp = "%.5f" % (1.0/sp) if n < 0 else "%.5f" % sp

        return float(sp)


class PowCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_pow(self):
        s = Solution()
        for i, o in [((0, 0), 1.00000),
                     ((-1.00001, 9), -1.00009),
                     ((1.00001, -3), 0.99997),
                     ((3, 2), 9.00000),
                     ((3.0, -2), 0.11111),
                     ((-4.0, -2), 0.06250),
                     ((0.00001, 2147483647), 0.00000),
                     ((-13.62608, 3), -2529.95504)]:
            self.assertEqual(s.myPow(i[0], i[1]), o)


if __name__ == '__main__':
    unittest.main()
