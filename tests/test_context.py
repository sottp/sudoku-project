import unittest
import clingo

from sudoku_board import Sudoku

from .partial_sudokus import DICTS, INITIAL

# This loads Context from sudoku6.py
# We need to replace clingo_main with a dummy function to avoid calling clingo when loading sudoku6.py if students did not write if __main__ == "__main__": in their code
clingo_main = clingo.application.clingo_main
clingo.application.clingo_main = lambda *args: None
from sudoku6 import Context
clingo.application.clingo_main = clingo_main


class TestSudoku(unittest.TestCase):
    def test_sudoku(self):
        for k, d in DICTS.items():
            sudoku = Sudoku(d)
            context = Context(sudoku)
            self.assertEqual(context.initial(), INITIAL[k], k)
