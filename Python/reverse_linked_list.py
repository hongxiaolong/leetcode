#!/usr/bin/env python
# encoding: utf-8

"""206. Reverse Linked List

Reverse a singly linked list.

Source : https://leetcode.com/problems/reverse-linked-list/
Author : hongxiaolong
Date   : 2016-10-06

"""

import unittest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        if not head:
            return None
        new_head = head
        node = head.next
        new_head.next = None
        while node:
            tmp = new_head
            new_head = node
            node = node.next
            new_head.next = tmp
        return new_head


class ReverseCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @staticmethod
    def array_to_list(arr):
        if not arr:
            return None
        head = ListNode(arr[0])
        node = head
        for i in xrange(1, len(arr)):
            node.next = ListNode(arr[i])
            node = node.next
        return head

    @staticmethod
    def list_to_array(lst):
        if not lst:
            return []
        arr = []
        node = lst
        while node:
            arr.append(node.val)
            node = node.next
        return arr

    def test_reverse_list(self):
        s = Solution()
        for arr in [[], [1], [1, 2], [1, 2, 3]]:
            lst = self.array_to_list(arr)
            reversed_lst = s.reverseList(lst)
            self.assertEqual(self.list_to_array(reversed_lst), arr[-1::-1])


if __name__ == "__main__":
    unittest.main()
