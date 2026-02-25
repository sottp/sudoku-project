import sys
from clingo.application import Application, clingo_main
from sudoku_board import Sudoku


class SudokuApp(Application):
    def main(self, ctl, files):

        for f in files:
            ctl.load(f)

        if not files:
            ctl.load("-")

        ctl.ground([("base", [])])
        ctl.solve()

    def print_model(self, model, printer):
        sudoku = Sudoku.from_model(model)
        print(sudoku)



if __name__ == "__main__":
    clingo_main(SudokuApp(), sys.argv[1:])

