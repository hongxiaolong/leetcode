#!/usr/bin/env python
# encoding: utf-8
import unittest


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and bin(n).count('1') == 1


class PowerTwoCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_power_of_two(self):
        s = Solution()
        for i, o in [(0, False),
                     (1, True),
                     (-1, False),
                     (16, True),
                     (65536, True)]:
            self.assertEqual(s.isPowerOfTwo(i), o)


if __name__ == '__main__':
    unittest.main()
