#!/usr/bin/env python
# encoding: utf-8
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
