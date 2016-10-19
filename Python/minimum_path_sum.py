# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""64. Minimum Path Sum

Given a m x n grid filled with non-negative numbers,
find a path from top left to bottom right which
minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Source : https://leetcode.com/problems/minimum-path-sum/
Author : hongxiaolong
Date   : 2016-10-19

"""


import unittest


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0

        dp = []
        m, n = len(grid), len(grid[0])

        for i in xrange(m):

            dp.append([0] * n)

            for j in xrange(n):

                if i == 0 and j == 0:
                    dp[0][0] = grid[0][0]
                    continue
                elif i == 0:
                    dp[0][j] = dp[0][j - 1]
                elif j == 0:
                    dp[i][0] = dp[i - 1][0]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1])
                dp[i][j] += grid[i][j]

        return dp[m - 1][n - 1]


class MinimumPathSumCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_minimum_path_sum(self):
        s = Solution()
        for i, o in [([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 21),
                     ([[]], 0),
                     ([[1]], 1),
                     ([[1, 2, 3]], 6),
                     ([[1, 2, 3], [4, 5, 6]], 12),
                     ([[1, 2], [1, 1]], 3)]:
            self.assertEqual(s.minPathSum(i), o)


if __name__ == '__main__':
    unittest.main()
