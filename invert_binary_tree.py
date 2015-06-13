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
    # @return {TreeNode}
    def invertTree(self, root):
        if not root:
            return root
        l, r = root.left, root.right
        root.left, root.right = r, l
        self.invertTree(l)
        self.invertTree(r)
        return root


class InvertTreeCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    # array = [#, 1, 2, 3, #, 4, 5, 6] and root.val = array[1]
    def _array_to_tree(self, array):
        if len(array) < 2:
            return None

        def _tree(node, array, i):
            if i * 2 < len(array) and array[i * 2] != '#':
                node.left = TreeNode(array[i * 2])
                _tree(node.left, array, i * 2)
            if i * 2 + 1 < len(array) and array[i * 2 + 1] != '#':
                node.right = TreeNode(array[i * 2 + 1])
                _tree(node.right, array, i * 2 + 1)
            
        root = TreeNode(array[1])
        _tree(root, array, 1)
        return root

    def _tree_to_array(self, root):
        if not root:
            return []
        
        # Level traverse
        l, q, node = [], [], root
        while node:
            l.append(node.val)
            left, right = node.left, node.right
            if left:
                q.insert(0, left)
            if right:
                q.insert(0, right)
            node = None if not q else q.pop()
        return l

    def test_invert_tree(self):
        s = Solution()
        for arr, ret in [([], []),
                         (['#'], []),
                         (['#', 1], [1]),
                         (['#', 1, 2], [1, 2]),
                         (['#', 1, 2, 4, '#', 3, 5, 6], 
                          [1, 4, 2, 6, 5, 3])]:
            tree = self._array_to_tree(arr)
            inverted_tree = s.invertTree(tree)
            array = self._tree_to_array(inverted_tree)
            self.assertEqual(array, ret)


if __name__ == '__main__':
    unittest.main()
