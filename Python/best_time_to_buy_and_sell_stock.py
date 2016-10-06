#!/usr/bin/env python
# encoding: utf-8

"""121. Best Time to Buy and Sell Stock

Say you have an array for which the ith element is
the price of a given stock on day i.

If you were only permitted to complete at most one transaction
(ie, buy one and sell one share of the stock),
design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5
(not 7-1 = 6, as selling price needs to be larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.

Source : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Author : hongxiaolong
Date   : 2016-10-06

"""

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
