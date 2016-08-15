#!/usr/bin/env python
# encoding: utf-8
import unittest


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, arr):

        self.root = self._arr_to_tree_(arr)

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


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def h(node):
            l, r = (0, 0), (0, 0)
            if node.left:
                l = h(node.left)
            if node.right:
                r = h(node.right)
            return (max(l) + 1, max(r) + 1)

        if not root:
            return True

        lh, rh = h(root)
        if abs(lh - rh) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)

        return False


class BlancedBinaryTreeCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_blanced_binary_tree(self):
        s = Solution()
        for arr, ret in [([], True),
                         ([0], True),
                         ([0, 1], True),
                         ([0, 1, 2], True),
                         ([0, 1, 2, None, 3, None, None, 4], False),
                         ([1, 2, 2, 3, None, None, 3, 4, None, None, 4],
                          False)]:
            tree = BinaryTree(arr)
            for i in xrange(len(arr) - 1, -1, -1):
                if arr[i] is None:
                    arr.pop()
                    continue
                break
            self.assertEqual(s.isBalanced(tree.root), ret)


if __name__ == '__main__':
    unittest.main()
