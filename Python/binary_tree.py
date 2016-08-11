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
        self.arr = self._tree_to_arr_(self.root)

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


class BinaryTreeCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_binary_tree(self):
        for arr in [[], [0], [0, 1], [0, 1, 2], [0, 1, None, None, None],
                    [0, 1, 2, None, 3, None, 4],
                    [0, 1, 2, None, 3, None, 4, None, None, 6,  None, 7, 8]]:
            tree = BinaryTree(arr)
            for i in xrange(len(arr) - 1, -1, -1):
                if arr[i] is None:
                    arr.pop()
                    continue
                break
            self.assertEqual(arr, tree.arr)


if __name__ == '__main__':
    unittest.main()

