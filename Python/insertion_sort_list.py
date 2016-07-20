#! /usr/bin/env python
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
    def insertionSortList(self, head):
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        curr = head
        while curr.next:
            if curr.next.val < curr.val:
                pre = dummy
                while pre.next.val < curr.next.val:
                    pre = pre.next
                tmp = curr.next
                curr.next = tmp.next
                tmp.next = pre.next
                pre.next = tmp
            else:
                curr = curr.next
        return dummy.next


class InsertionCase(unittest.TestCase):
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

    def _list_to_array(self, lst):
        if not lst:
            return []
        arr = []
        node = lst
        while node:
            arr.append(node.val)
            node = node.next
        return arr

    def test_insertion_sort_list(self):
        s = Solution()
        for arr in [[], [1], [1, 3, 2], [0, 1, 1, 2], [1, -2, 3, 0],
                    [4, 19, 14, 5, -3, 1, 8, 5, 11, 15]]:
            lst = self._array_to_list(arr)
            reversed_lst = s.insertionSortList(lst)
            ret = self._list_to_array(reversed_lst)
            self.assertEqual(ret, sorted(arr))


if __name__ == "__main__":
    unittest.main()
