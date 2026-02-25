import unittest

import clingo

from sudoku_board import Sudoku
from tests.full_sudokus import DICTS

INSTANCES = "./instances/"


def facts(d: dict[(int, int), int]) -> str:
    s = ""
    for (i, j), v in d.items():
        s += f"sudoku({i}, {j}, {v})."
    return s


class TestSudokuStr(unittest.TestCase):
    def test_sudoku(self):
        for instance, d in enumerate(DICTS):
            ctl = clingo.Control()
            ctl.add(facts(d))
            ctl.ground()
            with ctl.solve(yield_=True) as handle:
                for model in handle:
                    sudoku = Sudoku.from_model(model)
                    self.assertEqual(sudoku.sudoku, d, f"Failed on instance {instance}")
