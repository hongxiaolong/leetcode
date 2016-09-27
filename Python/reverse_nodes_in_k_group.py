#!/usr/bin/env python
# encoding: utf-8

"""25. Reverse Nodes in k-Group

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Source : https://leetcode.com/problems/reverse-nodes-in-k-group/
Author : hongxiaolong
Date   : 2016-09-27

"""

import unittest


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or k < 2:
            return head

        node, tail, head = head, head, None
        while node:
            n, h, t, i = node, None, node, 0
            while i < k and node:
                n, node.next = node.next, None
                l = h
                h, h.next = node, l
                node, i = n, i + 1

            if i == k:
                if head is None and node is None:
                    head = h
                    break
                elif head is None:
                    head = h

                tail.next = h
                tail = t
                continue

            node, h = h, None
            while node:
                n, node.next = node.next, None
                l = h
                h, h.next = node, l
                node = n

            if head is None:
                head = h
                break

            tail.next = h

        return head


class ReverseKGroupCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def array_to_list(self, arr):
        if not arr:
            return None
        head = ListNode(arr[0])
        node = head
        for i in xrange(1, len(arr)):
            node.next = ListNode(arr[i])
            node = node.next
        return head

    def list_to_array(self, head):
        if not head:
            return []
        arr = []
        node = head
        while node:
            arr.append(node.val)
            node = node.next
        return arr

    def test_reverse_k_group(self):
        s = Solution()
        for i, o in [(([1, 2, 3, 4, 5], 6), [1, 2, 3, 4, 5]),
                     (([1, 2, 3, 4, 5], 2), [2, 1, 4, 3, 5]),
                     (([1, 2, 3, 4, 5], 3), [3, 2, 1, 4, 5]),
                     (([1, 2], 0), [1, 2]),
                     (([1, 2, 3], 1), [1, 2, 3]),
                     (([1, 2], 2), [2, 1]),
                     (([1, 2, 3, 4], 2), [2, 1, 4, 3])]:
            head = self.array_to_list(i[0])
            arr = self.list_to_array(s.reverseKGroup(head, i[1]))
            self.assertEqual(arr, o)


if __name__ == '__main__':
    unittest.main()
