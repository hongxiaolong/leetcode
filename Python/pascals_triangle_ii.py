#!/usr/bin/env python
# encoding: utf-8

"""119. Pascal's Triangle II

Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?

Source : https://leetcode.com/problems/pascals-triangle-ii/
Author : hongxiaolong
Date   : 2016-09-18

"""

import unittest

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        def pt():
            a = [1]
            while True:
                yield a
                a = [sum(i) for i in zip([0] + a, a + [0])]

        row = []
        p = pt()
        for i in xrange(rowIndex + 1):
            row = p.next()
        return row


class PascalCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_pascal(self):
        s = Solution()
        for i, o in [(0, [1]),
                     (1, [1, 1]),
                     (2, [1, 2, 1]),
                     (3, [1, 3, 3, 1]),
                     (9, [1, 9, 36, 84, 126, 126, 84, 36, 9, 1])]:
            self.assertEqual(s.getRow(i), o)


if __name__ == '__main__':
    unittest.main()
