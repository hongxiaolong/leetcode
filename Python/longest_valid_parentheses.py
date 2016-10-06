#!/usr/bin/env python
# encoding: utf-8

"""32. Longest Valid Parentheses

Given a string containing just the characters '(' and ')',
find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()",
which has length = 2.

Another example is ")()())", where the longest valid parentheses
substring is "()()", which has length = 4.

Source : https://leetcode.com/problems/longest-valid-parentheses/
Author : hongxiaolong
Date   : 2016-10-06

"""

import unittest


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = 0
        stack = []
        for i in xrange(len(s)):
            if s[i] == "(":
                stack.append(("(", i))
            else:
                if len(stack) > 0 and stack[len(stack) - 1][0] == "(":
                    # 可以匹配，将(出栈
                    stack.pop()
                    if (len(stack) == 0):
                        # 如果栈为空，则说明所有括号()正好完整匹配
                        longest = i + 1
                    else:
                        # 如果栈不为空，说明只能部分匹配，该部分匹配的最长长度为当前位置减去栈顶)的位置
                        longest = max(longest, i - stack[len(stack) - 1][1])
                else:
                    # 将)和其位置入栈
                    stack.append((")", i))

        return longest


class LongestValidParenthesesCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_longes_valid_parentheses(self):
        s = Solution()
        for a, b in [("", 0),
                     ("(()", 2),
                     (")()())", 4),
                     (")()())((())()())", 10),
                     ("))))))((((((())))))(((((((((()())((())()())", 16)]:
            self.assertEqual(s.longestValidParentheses(a), b)


if __name__ == '__main__':
    unittest.main()
