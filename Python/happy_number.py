#!/usr/bin/env python
# encoding: utf-8

"""202. Happy Number

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum
of the squares of its digits, and repeat the process until the number
equals 1 (where it will stay), or it loops endlessly in a cycle
which does not include 1.
Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

Source : https://leetcode.com/problems/happy-number/
Author : hongxiaolong
Date   : 2016-10-06

"""

import unittest


class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        result = set()
        num = n
        while True:
            sum = self._sqr_sum(num)
            if sum in result:
                return False
            elif 1 == sum:
                return True
            result.add(sum)
            num = sum

    def _sqr_sum(self, n):
        digit, sum = n, 0
        while True:
            digit, remainder = digit / 10, digit % 10
            sum += remainder ** 2
            if not digit:
                break
        return sum


class HappyCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_happy(self):
        s = Solution()
        for i in (0, 2, 3):
            self.assertFalse(s.isHappy(i))

        for i in (1, 19):
            self.assertTrue(s.isHappy(i))


if __name__ == '__main__':
    unittest.main()
