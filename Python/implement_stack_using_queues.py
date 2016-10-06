#!/usr/bin/env python
# encoding: utf-8

"""225. Implement Stack using Queues

Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Notes:
You must use only standard operations of a queue --
which means only push to back, peek/pop from front,
size, and is empty operations are valid.
Depending on your language, queue may not be supported natively.
You may simulate a queue by using a list or deque (double-ended queue),
as long as you use only standard operations of a queue.
You may assume that all operations are valid
(for example, no pop or top operations will be called on an empty stack).

Update (2015-06-11):
The class name of the Java function had been updated to MyStack instead of Stack.

Source : https://leetcode.com/problems/implement-stack-using-queues/
Author : hongxiaolong
Date   : 2016-10-06

"""

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


class StackCase(unittest.TestCase):
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
