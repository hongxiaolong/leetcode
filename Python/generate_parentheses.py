#!/usr/bin/env python
# encoding: utf-8

"""22. Generate Parentheses

Given n pairs of parentheses,
write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

Source : https://leetcode.com/problems/generate-parentheses/
Author : hongxiaolong
Date   : 2016-09-08

"""

import unittest


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def gp(l, r, s, lst):
            if r < l:
                return
            if l == 0 and r == 0:
                lst.append(s)
            if l > 0:
                gp(l - 1, r, s + "(", lst)
            if r > 0:
                gp(l, r - 1, s + ")", lst)

        if n == 0:
            return []

        lst = []
        gp(n, n, "", lst)

        return lst


class ParenthesisCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_generate_parenthesis(self):
        s = Solution()
        for i, o in [(0, []),
                     (1, ["()"]),
                     (2, ["(())", "()()"]),
                     (3, ['((()))', '(()())', '(())()', '()(())', '()()()'])]:
            self.assertEqual(s.generateParenthesis(i), o)


if __name__ == '__main__':
    unittest.main()
