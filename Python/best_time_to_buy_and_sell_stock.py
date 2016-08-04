#!/usr/bin/env python
# encoding: utf-8
import unittest


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0

        mi, ma = prices[0], 0
        for i in xrange(1, len(prices)):
            mi = min(mi, prices[i])
            ma = max(ma, prices[i] - mi)
        return ma


class StockCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_stock(self):
        s = Solution()
        for a, b in [([], 0),
                     ([10], 0),
                     ([7, 1, 5, 3, 6, 4], 5),
                     ([7, 6, 4, 3, 1], 0)]:
            self.assertEqual(s.maxProfit(a), b)


if __name__ == '__main__':
    unittest.main()
