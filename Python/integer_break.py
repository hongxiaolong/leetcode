#!/usr/bin/env python
# encoding: utf-8
import unittest


class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2 or n == 3:
            return n - 1
        r = 1
        while(n > 4):
            r *= 3
            n -= 3
        return r * n



class BinaryCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_add_binary(self):
        s = Solution()
        for n, r in [(2, 1), (10, 36), (8, 18), (58, 1549681956)]:
            self.assertEqual(s.integerBreak(n), r)


if __name__ == '__main__':
    unittest.main()
