#!/usr/bin/env python
# encoding: utf-8

"""191. Number of 1 Bits

Write a function that takes an unsigned integer and returns the number of ’1'
bits it has (also known as the Hamming weight).

For example, the 32-bit integer ’11' has binary representation
00000000000000000000000000001011, so the function should return 3.

Source : https://leetcode.com/problems/number-of-1-bits/
Author : hongxiaolong
Date   : 2016-10-06

"""

import unittest


class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        if n < 0:
            return 0
        nums = 0
        while n:
            nums += n & 1
            n >>= 1
        return nums


class HammingCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_hamming(self):
        s = Solution()
        for n, ret in [(-1, 0), (0, 0), (1, 1), (3, 2), (11, 3)]:
            self.assertEqual(s.hammingWeight(n), ret)


if __name__ == "__main__":
    unittest.main()
