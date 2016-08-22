#! /usr/bin/env python
# encoding: utf-8
import unittest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class ListNodes(object):

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

    def reverse(self, head):
        now, rhead = head, []
        while now:
            node, now = now, now.next
            node.next, rhead = rhead, node
        return rhead

    def mid(self, head):
        if not head:
            return None
        if not head.next:
            return head

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


class ListNodesCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_arr_to_list(self):
        for arr in [[], [1], [1, 3, 2], [0, 1, 1, 2], [1, -2, 3, 0],
                    [4, 19, 14, 5, -3, 1, 8, 5, 11, 15]]:
            lns = ListNodes()
            head = lns.array_to_list(arr)
            self.assertEqual(lns.list_to_array(head), arr)

    def test_mid(self):
        for arr, m in [([], None),
                         ([1], 1),
                         ([0, 1], 0),
                         ([1, 2, 3], 2),
                         ([1, -2, 3, 0], -2),
                         ([4, 19, 14, 5, -3, 0, 1, 8, 5, 11, 15], 0)]:
            lns = ListNodes()
            head = lns.array_to_list(arr)
            mid = lns.mid(head)
            if m is None:
                self.assertIsNone(mid)
                continue

            self.assertEqual(mid.val, m)

    def test_reverse(self):
        for arr, rarr in [([], []),
                          ([1], [1]),
                          ([0, 1], [1, 0]),
                          ([1, 2, 3], [3, 2, 1])]:
            lns = ListNodes()
            head = lns.array_to_list(arr)
            rhead = lns.reverse(head)
            self.assertEqual(lns.list_to_array(rhead), rarr)


if __name__ == "__main__":
    unittest.main()
