#!/usr/bin/env python
# encoding: utf-8

"""100. Same Tree

Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical
and the nodes have the same value.

Source : https://leetcode.com/problems/same-tree/
Author : hongxiaolong
Date   : 2016-10-06

"""

import unittest


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def eq(p, q):
            if (not p and not q):
                return True
            if (not p or not q or p.val != q.val):
                return False
            return eq(p.left, q.left) and eq(p.right, q.right)

        return eq(p, q)


class SameTreeCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    # arr = [#,1,#,2,#,#,3] and root.val = arr[1]
    def _array_to_tree(self, arr):
        if len(arr) <= 1:
            return None

        def _tree(node, arr, i):
            if 2 * i < len(arr) and arr[2 * i] != '#':
                node.left = TreeNode(arr[2 * i])
                _tree(node.left, arr, 2 * i)
            if 2 * i + 1 < len(arr) and arr[2 * i + 1] != '#':
                node.right = TreeNode(arr[2 * i + 1])
                _tree(node.right, arr, 2 * i + 1)
            return node

        root = TreeNode(arr[1])
        return _tree(root, arr, 1)

    def test_same_tree(self):
        s = Solution()
        for a, b, c in [(['#'], ['#'], True),
                        ([0], [0], True),
                        ([0, 1], [0, 1], True),
                        ([0, '#', 1], [0, '#', 1], True),
                        ([0, '#', 1, 2], [0, '#', 1, 2], True),
                        ([0, '#', 1, '#', 2], [0, '#', 1, '#', 3], False),
                        ([0, '#', 1, '#', 2], [0, '#', 1, 2], False)]:
            self.assertEqual(s.isSameTree(
                self._array_to_tree(a), self._array_to_tree(b)), c)


if __name__ == '__main__':
    unittest.main()
