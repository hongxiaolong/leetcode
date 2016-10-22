# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""372. Super Pow

Your task is to calculate ab mod 1337 where a is a positive integer
and b is an extremely large positive integer given in the form of an array.

Example1:

a = 2
b = [3]

Result: 8
Example2:

a = 2
b = [1,0]

Result: 1024

Source : https://leetcode.com/problems/super-pow/
Author : hongxiaolong
Date   : 2016-10-22

"""


import unittest


class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        o, i = 1, a
        for n in b[::-1]:
            o = (o * self.quickPow(i, n, 1337)) % 1337
            i = self.quickPow(i, 10, 1337)
        return o

    def quickPow(self, a, b, m):
        o = 1
        while b > 0:
            if b & 1:
                o *= a
            a = (a * a) % m
            b >>= 1
        return o


class SuperPowCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_super_pow(self):
        s = Solution()
        for i, o in [((2, [3]), 8),
                     ((2, [1, 0]), 1024),
                     ((0, [0]), 1),
                     ((2, [2, 0, 4, 8, 0, 0]), 914)]:
            self.assertEqual(s.superPow(i[0], i[1]), o)


if __name__ == '__main__':
    unittest.main()
