#!/usr/bin/env python
# encoding: utf-8
import unittest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def sortList(self, head):
        if not head or not head.next:
            return head
        mid = self.find_mid(head)
        right = self.sortList(mid.next)
        mid.next = None
        left = self.sortList(head)
        return self.merge(left, right)

    def find_mid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, head1, head2):
        head = ListNode(0)
        lst = head
        while head1 and head2:
            if head1.val <= head2.val:
                lst.next = head1
                head1 = head1.next
            else:
                lst.next = head2
                head2 = head2.next
            lst = lst.next
        if head1:
            lst.next = head1
        else:
            lst.next = head2
        return head.next


class SortListCase(unittest.TestCase):
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

    def _list_to_array(self, links):
        if not links:
            return []
        array = []
        while links:
            array.append(links.val)
            links = links.next
        return array

    def test_sort_list(self):
        s = Solution()
        for arr in [[], [0], [3, -1, 0], [-10, 0, 1, 5]]:
            lst = self._array_to_link(arr)
            ret = s.sortList(lst)
            self.assertEqual(self._list_to_array(ret), sorted(arr))


if __name__ == '__main__':
    unittest.main()
