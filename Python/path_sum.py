#!/usr/bin/env python
# encoding: utf-8

"""112. Path Sum

Given a binary tree and a sum, determine if the tree has a root-to-leaf path
such that adding up all the values along the path equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

Source : https://leetcode.com/problems/path-sum/
Author : hongxiaolong
Date   : 2016-10-06

"""

import unittest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param {TreeNode} root
    # @param {integer} sum
    # @return {boolean}
    def hasPathSum(self, root, sum):
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == sum
        return self.hasPathSum(root.left, sum - root.val) \
            or self.hasPathSum(root.right, sum - root.val)


class PathSumCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_has_path_sum(self):
        s = Solution()

        empty_tree = None
        self.assertFalse(s.hasPathSum(empty_tree, 0))

        trees = TreeNode(1)
        self.assertFalse(s.hasPathSum(trees, 0))
        self.assertTrue(s.hasPathSum(trees, 1))

        trees = TreeNode(1)
        trees.left = TreeNode(2)
        self.assertFalse(s.hasPathSum(trees, 2))
        self.assertTrue(s.hasPathSum(trees, 3))


if __name__ == '__main__':
    unittest.main()
