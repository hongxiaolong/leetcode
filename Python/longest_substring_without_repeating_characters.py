#!/usr/bin/env python
# encoding: utf-8

"""3. Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring
without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3.

Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

Source : https://leetcode.com/problems/longest-substring-without-repeating-characters/
Author : hongxiaolong
Date   : 2016-11-01

"""

import unittest


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n < 2:
            return n

        lst, longest = [s[0]], 1
        for i in xrange(1, n):
            if s[i] not in lst:
                lst.append(s[i])
                continue

            m = len(lst)
            if m > longest:
                longest = m

            for j in xrange(m):
                if lst[j] == s[i]:
                    del lst[:j + 1]
                    lst.append(s[i])
                    break

        return max(longest, len(lst))


class IntersectionCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_intersection(self):
        s = Solution()
        for i, o in [("abcabcbb", len("abc")),
                     ("bbbbb", len("b")),
                     ("pwwkew", len("wke")),
                     ("au", len("au")),
                     ("dvdf", len("vdf")),
                     ("jbpnbwwd", len("jbpn"))]:
            self.assertEqual(s.lengthOfLongestSubstring(i), o)


if __name__ == '__main__':
    unittest.main()
