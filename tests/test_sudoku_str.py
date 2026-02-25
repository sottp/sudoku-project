import unittest

from sudoku_board import Sudoku
from tests.full_sudokus import DICTS, STRS

INSTANCES = "./instances/"


class TestSudokuStr(unittest.TestCase):
    def test_sudoku(self):
        for d, s in zip(DICTS, STRS):
            sudoku = Sudoku(d)
            s2 = [line.strip() for line in str(sudoku).strip().splitlines()]
            s3 = [line.strip() for line in s.strip().splitlines()]
            self.assertEqual(s2, s3)
