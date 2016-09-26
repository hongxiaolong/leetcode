#!/usr/bin/env python
# encoding: utf-8

"""290. Word Pattern

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection
between a letter in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.
Notes:
You may assume pattern contains only lowercase letters,
and str contains lowercase letters separated by a single space.

Source : https://leetcode.com/problems/word-pattern/
Author : hongxiaolong
Date   : 2016-09-26

"""

import unittest


class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        lst = str.split(' ')

        if len(lst) != len(pattern):
            return False

        d = {}
        for i in xrange(len(lst)):

            if lst[i] not in d:

                if pattern[i] in d.values():
                    return False

                d[lst[i]] = pattern[i]
                continue

            if lst[i] in d and d[lst[i]] != pattern[i]:
                return False

        return True


class WordPatternCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_word_pattern(self):
        s = Solution()
        for i, o in [(("abba", "dog cat cat dog"), True),
                     (("abba", "dog cat cat fish"), False),
                     (("aaaa", "dog cat cat dog"), False),
                     (("abba", "dog dog dog dog"), False),
                     (("abcba", "dog cat fish cat dog"), True),
                     (("e", "eukera"), True),
                     (("deadbeef", "d e a d b e e f"), True)]:
            self.assertEqual(s.wordPattern(i[0], i[1]), o)


if __name__ == '__main__':
    unittest.main()
