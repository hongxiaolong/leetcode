#!/usr/bin/env python
# encoding: utf-8

"""66. Plus One

Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.

Source : https://leetcode.com/problems/plus-one/
Author : hongxiaolong
Date   : 2016-10-06

"""

import unittest


class Solution:
    # @param {integer[]} digits
    # @return {integer[]}
    def plusOne(self, digits):
        if not digits:
            return []
        flag = 0
        for i in xrange(-1, -len(digits) - 1, -1):
            tmp = digits[i] + flag
            tmp = tmp if i != -1 else tmp + 1
            flag, digits[i] = tmp // 10, tmp % 10
        if flag:
            digits.insert(0, flag)
        return digits


class PlusOneCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_plus_one(self):
        s = Solution()
        for digits, ret in [([], []),
                            ([0], [1]),
                            ([1, 9], [2, 0]),
                            ([9, 9], [1, 0, 0]),
                            ([9, 0, 9], [9, 1, 0])]:
            self.assertEqual(s.plusOne(digits), ret)


if __name__ == '__main__':
    unittest.main()
