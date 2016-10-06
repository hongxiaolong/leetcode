#!/usr/bin/env python
# encoding: utf-8

"""6. ZigZag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
of rows like this:
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

Source : https://leetcode.com/problems/zigzag-conversion/
Author : hongxiaolong
Date   : 2016-10-06

"""

import unittest


class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        if not s or numRows < 2:
            return s
        ret = []
        numCols = len(s) // (2 * numRows - 2) + 1
        for i in xrange(numRows):
            for j in xrange(numCols):
                index = j * (2 * numRows - 2) + i
                if index < len(s):
                    if i == 0 or i == numRows - 1:
                        ret.append(s[index])
                        continue
                    ret.append(s[index])
                    if index + 2 * (numRows - 1 - i) < len(s):
                        ret.append(s[index + 2 * (numRows - 1 - i)])
        return ''.join(ret)


class ZigZagCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_zigzag_convert(self):
        s = Solution()
        for tar, rows, ret in [('', 1, ''),
                               ('P', 2, 'P'),
                               ('ABCDE', 4, 'ABCED'),
                               ('PAYPALISHIRING', 3, 'PAHNAPLSIIGYIR')]:
            self.assertEqual(s.convert(tar, rows), ret)


if __name__ == '__main__':
    unittest.main()
