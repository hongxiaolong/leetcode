#!/usr/bin/env python
# encoding: utf-8

"""224. Basic Calculator

Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ),
the plus + or minus sign -, non-negative integers and empty spaces .

You may assume that the given expression is always valid.

Some examples:
"1 + 1" = 2
" 2-1 + 2 " = 3
"(1+(4+5+2)-3)+(6+8)" = 23
Note: Do not use the eval built-in library function.

Source : https://leetcode.com/problems/basic-calculator/
Author : hongxiaolong
Date   : 2016-10-06

"""

import unittest


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        def subcal(s, p):
            """
            :type s: str
            :type p: int
            :rtype: (int, int)
            """
            r, o = [], 1
            while(p < len(s)):
                if (s[p] == ' '):
                    p = p + 1
                elif (s[p] == '('):
                    n, p = subcal(s, p + 1)
                    r.append(n * o)
                elif (s[p] == ')'):
                    break
                elif (s[p] == '+'):
                    o = 1
                    p = p + 1
                elif (s[p] == '-'):
                    o = -1
                    p = p + 1
                else:
                    n = []
                    while(p < len(s) and s[p].isdigit()):
                        n.insert(0, int(s[p]))
                        p = p + 1
                    for i in xrange(len(n)):
                        n[i] = n[i] * (10 ** i)
                    r.append(o * reduce(lambda x, y: x + y, n))

            return (reduce(lambda x, y: x + y, r), p + 1)

        return subcal(s, 0)[0]


class BasicCalculatorCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_calculate(self):
        s = Solution()
        for i, r in [("1 + 1", 2),
                     (" 2-1 + 2 ", 3),
                     ("(1+(4+5+2)-3)+(6+8)", 23),
                     (" 2147483647  ", 2147483647)]:
            self.assertEqual(s.calculate(i), r)


if __name__ == '__main__':
    unittest.main()
