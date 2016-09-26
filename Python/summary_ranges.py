#!/usr/bin/env python
# encoding: utf-8

"""228. Summary Ranges

Given a sorted integer array without duplicates,
return the summary of its ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].

Source : https://leetcode.com/problems/summary-ranges/
Author : hongxiaolong
Date   : 2016-09-22

"""

import unittest


class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        ranges = []
        first, last = nums[0], nums[0]
        for i in xrange(1, len(nums)):
            if nums[i] - last == 1:
                last = nums[i]
                continue
            if first != last:
                ranges.append("%d->%d" % (first, last))
            else:
                ranges.append("%d" % last)

            first, last = nums[i], nums[i]

        if first != last:
            ranges.append("%d->%d" % (first, last))
        else:
            ranges.append("%d" % last)

        return ranges


class SummaryRangesCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_summary_ranges(self):
        s = Solution()
        for i, o in [([0], ["0"]),
                     ([0, 1, 2], ["0->2"]),
                     ([0, 1, 2, 4, 5, 7], ["0->2", "4->5", "7"])]:
            self.assertEqual(s.summaryRanges(i), o)


if __name__ == '__main__':
    unittest.main()
