#!/usr/bin/env python
# encoding: utf-8

"""227. Basic Calculator II

Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators
and empty spaces . The integer division should truncate toward zero.

You may assume that the given expression is always valid.

Some examples:
"3+2*2" = 7
" 3/2 " = 1
" 3+5 / 2 " = 5
Note: Do not use the eval built-in library function.

Source : https://leetcode.com/problems/coin-change/
Author : hongxiaolong
Date   : 2016-08-19

"""

import unittest


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """

        # get number
        def gn(s, p):
            n = 0
            while p < len(s) and s[p] == ' ':
                p = p + 1
            while p < len(s) and s[p].isdigit():
                    n = n * 10 + int(s[p])
                    p = p + 1
            return n, p

        l, p = [], 0
        while p < len(s):
            if s[p] == ' ':
                p = p + 1
            elif s[p] == '+':
                n, p = gn(s, p + 1)
                l.append(n)
            elif s[p] == '-':
                n, p = gn(s, p + 1)
                l.append(-1 * n)
            elif s[p] == '*':
                n, p = gn(s, p + 1)
                l[-1] = l[-1] * n
            elif s[p] == '/':
                n, p = gn(s, p + 1)
                if l[-1] >= 0:
                    l[-1] = l[-1] / n
                elif l[-1] < 0:
                    l[-1] = (-1 * l[-1] / n) * -1
            else:
                n, p = gn(s, p)
                l.append(n)

        return reduce(lambda x, y: x + y, l)


class BasicCalculatorCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_calculate(self):
        s = Solution()
        for i, o in [("3+2*2", 7),
                     (" 3/2 ", 1),
                     (" 3+5 / 2 ", 5),
                     ("14-3/2", 13),
                     (" 2147483647  ", 2147483647)]:
            self.assertEqual(s.calculate(i), o)


if __name__ == '__main__':
    unittest.main()
