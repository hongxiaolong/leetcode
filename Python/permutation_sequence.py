# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""60. Permutation Sequence

The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.

Source : https://leetcode.com/problems/permutation-sequence/
Author : hongxiaolong
Date   : 2016-10-08

"""

import math
import unittest


class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = [str(i) for i in xrange(1, n + 1)]
        fac = math.factorial(n)
        k, s = k - 1, ""
        while n:
            fac = fac / n
            pos = k / fac
            s = s + nums[pos]
            del nums[pos]

            n, k = n - 1, k % fac

        return s


class ThreeSumCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_three_sum(self):
        s = Solution()
        for i, o in [((1, 1), "1"),
                     ((2, 1), "12"),
                     ((3, 3), "213"),
                     ((9, 10), "123457896")]:
            self.assertEqual(s.getPermutation(i[0], i[1]), o)


if __name__ == '__main__':
    unittest.main()
