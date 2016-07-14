#!/usr/bin/env python
# encoding: utf-8
import unittest


class Solution:
    def __init__(self):
        self.ret = []

    # @param {integer[]} nums
    # @return {integer[][]}
    def subsets(self, nums):
        if not len(nums):
            return []
        nums.sort()
        self.dfs(0, nums, [])
        ret = list(self.ret + [[]])
        self.ret = []
        return ret

    def dfs(self, pos, nums, lst):
        for i in xrange(pos, len(nums)):
            lst.append(nums[i])
            # Add combinations into result
            self.ret.append(list(lst))
            self.dfs(i + 1, nums, lst)
            lst.pop()


class SubsetsCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_subsets(self):
        s = Solution()
        for nums, ret in [([], []),
                          ([1], [[1], []]),
                          ([1, 2], [[1], [1, 2], [2], []]),
                          ([1, 2, 3], [[1], [1, 2], [1, 2, 3], [1, 3],
                                       [2], [2, 3], [3], []])]:
            self.assertEqual(s.subsets(nums), ret)


if __name__ == '__main__':
    unittest.main()
