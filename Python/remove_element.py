#!/usr/bin/env python
# encoding: utf-8
import unittest


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        l, r = len(nums), 0
        for i in xrange(l - 1, -1, -1):
            if nums[i] == val:
                del nums[i]
                r += 1
        return l - r


class RemoveElementCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_remove_element(self):
        s = Solution()
        for arr_bef, v, arr_aft, l in [
            ([3, 2, 2, 3], 3, [2, 2], 2),
            ([], 3, [], 0),
                ([3], 2, [3], 1)]:
            self.assertEqual(s.removeElement(arr_bef, v), l)
            self.assertListEqual(arr_bef, arr_aft)


if __name__ == '__main__':
    unittest.main()
