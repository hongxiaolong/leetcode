#!/usr/bin/env python
# encoding: utf-8

"""101. Symmetric Tree

Given a binary tree, check whether it is a mirror of itself
(ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.

Source : https://leetcode.com/problems/symmetric-tree/
Author : hongxiaolong
Date   : 2016-10-01

"""


import unittest


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def sym(left, right):
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False

            return sym(left.left, right.right) and sym(left.right, right.left)

        if root is None:
            return True

        return sym(root.left, root.right)


class SymmetricTreeCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def _arr_to_tree_(self, arr):

        if len(arr) < 1:
            return None

        root, pos = TreeNode(arr[0]), 1
        queue = [root]

        while len(queue) and pos < len(arr):
            node = queue.pop()
            if arr[pos]:
                node.left = TreeNode(arr[pos])
                queue.insert(0, node.left)
            pos += 1
            if pos < len(arr) and arr[pos]:
                node.right = TreeNode(arr[pos])
                queue.insert(0, node.right)
            pos += 1

        return root

    def _tree_to_arr_(self, root):

        if not root:
            return []

        queue, arr = [root], [root.val]

        while len(queue):
            node = queue.pop()
            if node.left:
                queue.insert(0, node.left)
                arr.append(node.left.val)
            else:
                arr.append(None)

            if node.right:
                queue.insert(0, node.right)
                arr.append(node.right.val)
            else:
                arr.append(None)

        for i in xrange(len(arr) - 1, -1, -1):
            if arr[i] is None:
                arr.pop()
                continue
            break

        return arr

    def test_symmetric_tree(self):
        s = Solution()
        for i, o in [([], True),
                     ([0], True),
                     ([0, 1], False),
                     ([0, 1, 2], False),
                     ([1, 2, 2, 3, 4, 4, 3], True),
                     ([1, 2, 2, 3, None, 4, 3], False),
                     ([1, 2, 2, None, 3, None, 3], False)]:
            root = self._arr_to_tree_(i)
            self.assertEqual(s.isSymmetric(root), o)


if __name__ == '__main__':
    unittest.main()
