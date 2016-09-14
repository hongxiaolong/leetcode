#!/usr/bin/env python
# encoding: utf-8

"""77. Combinations

Given two integers n and k,
return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

Source : https://leetcode.com/problems/combinations/
Author : hongxiaolong
Date   : 2016-09-13

"""

import unittest


class Solution(object):

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n < 2:
            return [1]

        self.res = []
        tmp = []
        self.dfs(n, k, 1, 0, tmp)
        return self.res

    def dfs(self, n, k, m, p, tmp):
        if k == p:
            self.res.append(tmp[:])
            return
        for i in range(m, n + 1):
            tmp.append(i)
            self.dfs(n, k, i + 1, p + 1, tmp)
            tmp.pop()


class CombineCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_combine(self):
        s = Solution()
        for i, o in [((1, 1), [1]),
                     ((2, 2), [[1, 2]]),
                     ((3, 2), [[1, 2], [1, 3], [2, 3]]),
                     ((4, 3), [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]])]:
            self.assertEqual(s.combine(i[0], i[1]), o)


if __name__ == '__main__':
    unittest.main()
