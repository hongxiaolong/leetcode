#!/usr/bin/env python
# encoding: utf-8

"""2. Add Two Numbers

You are given two linked lists representing two non-negative numbers.
The digits are stored in reverse order and each of their nodes contain
a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

Source : https://leetcode.com/problems/add-two-numbers/
Author : hongxiaolong
Date   : 2016-09-02

"""

import unittest


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2

        if not l2:
            return l1

        node1, node2 = l1, l2

        head = ListNode(0)
        node = head
        carry = 0

        while node1 or node2:

            if node1 and node2:
                n = node1.val + node2.val
                node1, node2 = node1.next, node2.next
            elif node1:
                n = node1.val
                node1 = node1.next
            elif node2:
                n = node2.val
                node2 = node2.next

            n = n + carry
            carry = n / 10

            node.next = ListNode(n % 10)
            node = node.next

        if carry:
            node.next = ListNode(carry)

        return head.next


class AddCase(unittest.TestCase):
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

    def test_add_two_numbers(self):
        s = Solution()
        for i, o in [(([], []), []),
                     (([0], [1]), [1]),
                     (([1, 8], [0]), [1, 8]),
                     (([2, 4, 3], [5, 6, 4]), [7, 0, 8]),
                     (([0, 1], [9, 9, 9, 9]), [9, 0, 0, 0, 1])]:
            head = s.addTwoNumbers(self._array_to_list(
                i[0]), self._array_to_list(i[1]))
            arr = self._list_to_array(head)
            self.assertEqual(arr, o)


if __name__ == '__main__':
    unittest.main()
