#!/usr/bin/env python
# encoding: utf-8

"""36. Valid Sudoku

Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.


A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable.
Only the filled cells need to be validated.

Source : https://leetcode.com/problems/valid-sudoku/
Author : hongxiaolong
Date   : 2016-10-06

"""

import unittest


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row = [set([]) for i in range(9)]
        col = [set([]) for i in range(9)]
        grid = [set([]) for i in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if board[r][c] in row[r]:
                    return False
                if board[r][c] in col[c]:
                    return False

                g = r / 3 * 3 + c / 3
                if board[r][c] in grid[g]:
                    return False
                grid[g].add(board[r][c])
                row[r].add(board[r][c])
                col[c].add(board[r][c])

        return True


class SudokuCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_sudoku(self):
        s = Solution()
        for a, b in [([".87654321", "2........", "3........",
                       "4........", "5........", "6........",
                       "7........", "8........", "9........"], True),
                     (["..4...63.", ".........", "5......9.",
                       "...56....", "4.3.....1", "...7.....",
                       "...5.....", ".........", "........."], False)]:
            self.assertEqual(s.isValidSudoku(a), b)


if __name__ == '__main__':
    unittest.main()
