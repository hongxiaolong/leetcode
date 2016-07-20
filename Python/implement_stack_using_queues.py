#!/usr/bin/env python
# encoding: utf-8
import unittest


class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[len(self.stack) - 1]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stack) == 0


class BinaryCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_push(self):
        s = Stack()
        l = [-1, 0, 1, 1, 10, 100]
        for x in l:
            s.push(x)
        self.assertListEqual(s.stack, l)

    def test_pop(self):
        s = Stack()
        l = [-1, 0, 1, 10, 100]
        for x in l:
            s.push(x)
        for i in xrange(len(l)):
            s.pop()
            l.pop()
            self.assertListEqual(s.stack, l)

    def test_top(self):
        s = Stack()
        l = [-1, 0, 1, 10, 100]
        for x in l:
            s.push(x)
            self.assertEqual(s.top(), x)

    def test_empty(self):
        s = Stack()
        self.assertEqual(s.empty(), True)
        s.push(0)
        self.assertEqual(s.empty(), False)
        s.pop()
        self.assertEqual(s.empty(), True)

if __name__ == '__main__':
    unittest.main()
