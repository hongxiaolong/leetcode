#!/usr/bin/env python
# encoding: utf-8
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
