#!/usr/bin/env python
# encoding: utf-8
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
