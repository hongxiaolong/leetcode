#!/usr/bin/env python
# encoding: utf-8

"""304. Range Sum Query 2D - Immutable

Given a 2D matrix matrix, find the sum of the elements
inside the rectangle defined by its upper left corner (row1, col1)
and lower right corner (row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1)
and (row2, col2) = (4, 3), which contains sum = 8.

Example:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12
Note:
You may assume that the matrix does not change.
There are many calls to sumRegion function.
You may assume that row1 ≤ row2 and col1 ≤ col2.


Source : https://leetcode.com/problems/range-sum-query-2d-immutable/
Author : hongxiaolong
Date   : 2016-10-06

"""


import unittest


class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        r = len(matrix)
        if r < 1:
            self.matrix = []
            return

        c = len(matrix[0])
        if c < 1:
            self.matrix = [[]] * r
            return

        self.matrix = []

        i, j, l = 0, 0, []
        while i < r:

            while j < c:
                if i == 0 and j == 0:
                    l.append(matrix[i][j])
                elif i == 0:
                    l.append(matrix[i][j] + l[-1])
                elif j == 0:
                    l.append(self.matrix[i - 1][j] + matrix[i][j])
                else:
                    l.append(self.matrix[i - 1][j] + matrix[i][j] + l[-1]
                        - self.matrix[i - 1][j - 1])
                j += 1

            self.matrix.append(l)

            i, j, l = i + 1, 0, []



    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        r = len(self.matrix)
        if r < 1:
            return 0

        c = len(self.matrix[0])
        if c < 1:
            return 0

        if row1 > r or row2 < 0:
            return 0

        if col1 > c or col2 < 0:
            return 0

        if row1 == 0 and col1 == 0:
            return self.matrix[row2][col2]
        elif row1 == 0:
            return (self.matrix[row2][col2]
                        - self.matrix[row2][col1 - 1])
        elif col1 == 0:
            return (self.matrix[row2][col2]
                        - self.matrix[row1 - 1][col2])

        return (self.matrix[row2][col2]
                    - self.matrix[row2][col1 - 1]
                    - self.matrix[row1 - 1][col2]
                    + self.matrix[row1 - 1][col1 - 1])


class NumMatrixCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_sum_region(self):
        matrix = [[3, 0, 1, 4, 2],
                  [5, 6, 3, 2, 1],
                  [1, 2, 0, 1, 5],
                  [4, 1, 0, 1, 7],
                  [1, 0, 3, 0, 5]]
        m = NumMatrix(matrix)
        for i, o in [([2, 1, 4, 3], 8),
                     ([1, 1, 2, 2], 11),
                     ([1, 2, 2, 4], 12)]:
            self.assertEqual(m.sumRegion(i[0], i[1], i[2], i[3]), o)


if __name__ == '__main__':
    unittest.main()
