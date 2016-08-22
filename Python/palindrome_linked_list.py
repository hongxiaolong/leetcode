#!/usr/bin/env python
# encoding: utf-8

"""234. Palindrome Linked List

Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?

Source : https://leetcode.com/problems/palindrome-linked-list/
Author : hongxiaolong
Date   : 2016-08-22

"""

import unittest


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def find_mid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverse(self, head):
        now, rhead = head, None
        while now:
            node, now = now, now.next
            node.next, rhead = rhead, node
        return rhead

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True

        mid = self.find_mid(head)
        l, r = head, self.reverse(mid.next)
        while r:
            if (l.val != r.val):
                return False
            l, r = l.next, r.next

        return True


class PalindromeCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def _array_to_link(self, array):
        if len(array) < 1:
            return None
        head = ListNode(array[0])
        lst = head
        for i in xrange(1, len(array)):
            lst.next = ListNode(array[i])
            lst = lst.next
        return head

    def test_palindrome(self):
        s = Solution()
        for i, o in [([], True),
                     ([0], True),
                     ([1, 1], True),
                     ([1, 2], False),
                     ([1, 2, 1], True),
                     ([1, 2, 2, 1], True),
                     ([1, 2, 3, 3, 1], False)]:
            self.assertEqual(s.isPalindrome(self._array_to_link(i)), o)


if __name__ == '__main__':
    unittest.main()
