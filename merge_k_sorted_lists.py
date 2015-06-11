#!/usr/bin/env python
# encoding: utf-8
import unittest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param {ListNode[]} lists
    # @return {ListNode}
    def mergeKLists(self, lists):
        l = len(lists)

        if l == 0:
            return None
        if l == 1:
            return lists[0]

        mid = l / 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        l, r = left, right
        head = ListNode(0)
        lst = head
        while l and r:
            if l.val <= r.val:
                lst.next = l
                l = l.next
            else:
                lst.next = r
                r = r.next
            lst = lst.next
        lst.next = l if l else r
        return head.next


class MergeCase(unittest.TestCase):
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

    def test_merge(self):
        s = Solution()
        self.assertEqual(s.mergeKLists([]), None)
        self.assertEqual(s.mergeKLists([None]), None)

        for arr, ret in [([[0]], [0]),
                         ([[-1], [0]], [-1, 0]),
                         ([[-1, 3], [0, 5]], [-1, 0, 3, 5]),
                         ([[-1, 3, 4], [-1, 3, 4], [-1, 0, 5]],
                          [-1, -1, -1, 0, 3, 3, 4, 4, 5])]:
            lst = []
            for i in arr:
                lst.append(self._array_to_link(i))
            result = s.mergeKLists(lst)
            self.assertEqual(self._list_to_array(result), ret)


if __name__ == '__main__':
    unittest.main()
