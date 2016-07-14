#!/usr/bin/env python
# encoding: utf-8
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
