#!/usr/bin/env python
# encoding: utf-8

"""19. Remove Nth Node From End of List

Given a linked list, remove the nth node from the end of list
and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end,
   the linked list becomes 1->2->3->5.

Note:
Given n will always be valid.
Try to do this in one pass.

Source : https://leetcode.com/problems/remove-nth-node-from-end-of-list/
Author : hongxiaolong
Date   : 2016-08-26

"""

import unittest


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return head

        node = head
        index, lst = 0, []
        while node:
            lst.append(node)
            index += 1
            node = node.next

        if n > index:
            return head
        elif n == index:
            return head.next
        else:
            lst[index - n - 1].next = lst[index - n].next

        return head


class RemoveNthFromEndCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def _array_to_list(self, arr):
        if not arr:
            return None
        head = ListNode(arr[0])
        node = head
        for i in xrange(1, len(arr)):
            node.next = ListNode(arr[i])
            node = node.next
        return head

    def _list_to_array(self, head):
        if not head:
            return []
        arr = []
        node = head
        while node:
            arr.append(node.val)
            node = node.next
        return arr

    def test_remove(self):
        s = Solution()
        for i, o in [(([], 0), []),
                     (([0], 1), []),
                     (([0], 2), [0]),
                     (([1, 2], 2), [2]),
                     (([1, 2, 3, 3, 1], 1), [1, 2, 3, 3])]:
            rhead = s.removeNthFromEnd(self._array_to_list(i[0]), i[1])
            rarr = self._list_to_array(rhead)
            self.assertEqual(rarr, o)


if __name__ == '__main__':
    unittest.main()
