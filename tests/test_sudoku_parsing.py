import os
import unittest

from sudoku_board import Sudoku
from tests.partial_sudokus import DICTS

INSTANCES = "./instances/txt"


class TestFromStr(unittest.TestCase):
    def assert_sudoku_str(self, sudoku_str: str):
        sudoku = Sudoku.from_str(sudoku_str)
        s2 = [line.strip() for line in str(sudoku).strip().splitlines()]
        s3 = [line.strip() for line in sudoku_str.strip().splitlines()]
        self.assertEqual(s2, s3)

    def assert_sudoku_dict(self, sudoku_str: str, file: str):
        sudoku = Sudoku.from_str(sudoku_str)
        self.assertEqual(sudoku.sudoku, DICTS[file])

    def test_sudoku(self):
        for file in os.listdir(INSTANCES):
            if file.endswith(".txt"):
                with open(os.path.join(INSTANCES, file), "r") as f:
                    sudoku_str = f.read()
                    self.assert_sudoku_dict(sudoku_str, file)
                    # self.assert_sudoku_str(sudoku_str)
