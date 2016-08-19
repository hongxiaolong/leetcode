#!/usr/bin/env python
# encoding: utf-8

"""322. Coin Change

You are given coins of different denominations and a total amount of money
amount. Write a function to compute the fewest number of coins that you need
to make up that amount. If that amount of money cannot be made up by any
combination of the coins, return -1.

Example 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)

Example 2:
coins = [2], amount = 3
return -1.

Note:
You may assume that you have an infinite number of each kind of coin.

Source : https://leetcode.com/problems/coin-change/
Author : hongxiaolong
Date   : 2016-08-19

"""

import unittest


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [0] + [-1] * amount
        for i in range(amount):
            if dp[i] < 0:
                continue
            for c in coins:
                if i + c > amount:
                    continue
                if dp[i + c] < 0 or dp[i + c] > dp[i] + 1:
                    dp[i + c] = dp[i] + 1
        return dp[amount]


class CoinChangeCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_coin_change(self):
        s = Solution()
        for i, o in [(([], 1), -1),
                     (([1], 2), 2),
                     (([2], 3), -1),
                     (([1, 2, 5], 11), 3)]:
            self.assertEqual(s.coinChange(i[0], i[1]), o)


if __name__ == '__main__':
    unittest.main()
