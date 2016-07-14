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
    # @return {integer[]}
    def preorderTraversal(self, root):
        if not root:
            return []
        lst = []
        self.traverse(root, lst)
        return lst

    def traverse(self, root, lst):
        if not root:
            return
        lst.append(root.val)
        if root.left:
            self.traverse(root.left, lst)
        if root.right:
            self.traverse(root.right, lst)


class PreorderCase(unittest.TestCase):
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

    def test_preorder(self):
        s = Solution()
        for arr, ret in [(['#'], []),
                         (['#', 0], [0]),
                         (['#', 1, '#', 2, '#', '#', 3], [1, 2, 3])]:
            tree = self._array_to_tree(arr)
            self.assertEqual(s.preorderTraversal(tree), ret)


if __name__ == '__main__':
    unittest.main()
