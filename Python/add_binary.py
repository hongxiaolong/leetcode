# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""67. Add Binary

Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".

Source : https://leetcode.com/problems/add-binary/
Author : hongxiaolong
Date   : 2016-10-06

"""

import unittest


class Solution:
    # @param {string} a
    # @param {string} b
    # @return {string}
    def addBinary(self, a, b):
        la, lb = len(a), len(b)
        pos, flag = 0, 0
        longer = list(a) if la >= lb else list(b)
        while pos + la and pos + lb:
            pos = pos - 1
            if int(a[pos]) and int(b[pos]):
                longer[pos] = unicode(flag)
                flag = 1
            elif int(a[pos]) or int(b[pos]):
                longer[pos] = unicode((flag + 1) % 2)
                flag = flag % 2
            else:
                longer[pos] = unicode(flag)
                flag = 0
        if flag:
            ll = len(longer)
            pos = pos - 1
            while pos + ll >= 0:
                if int(longer[pos]):
                    longer[pos] = u'0'
                    pos = pos - 1
                else:
                    longer[pos] = u'1'
                    break
            if pos + ll < 0:
                longer.insert(0, u'1')
        return ''.join(longer)


class BinaryCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_add_binary(self):
        s = Solution()
        for a, b, c in [('', '', ''),
                        ('', '010', '010'),
                        ('010', '010', '100'),
                        ('110', '110', '1100'),
                        ('110010', '10111', '1001001'),
                        ('101111', '10', '110001')]:
            self.assertEqual(s.addBinary(a, b), c)


if __name__ == '__main__':
    unittest.main()
