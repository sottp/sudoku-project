from clingo.application import Application, clingo_main
from sudoku_board import Sudoku

import sys
import shutil
import clingo

def lpCombine():
    destination = "sudoku_py.lp"
    append_file = "instances/lp/ex00.lp"

    if len(sys.argv) == 2:
        append_file = sys.argv[1]

    open(destination, "w").close()  # wipe

    shutil.copyfile("sudoku.lp", destination)
    with open(append_file, "r") as f_in, open(destination, "a") as f_out:
        f_out.write(f_in.read())

class SudokuApp(Application):
    def main(self, ctl, files):
        lpCombine()

        ctl.load("sudoku_py.lp")

        for f in files:
            ctl.load(f)

        ctl.ground([("base", [])])
        ctl.solve()

    def print_model(self, model, printer):
        sudoku = Sudoku.from_model(model)
        print(sudoku)

    class Context:
        def __init__(self, board: Sudoku):
            self.board = board

        def initial(self) -> list[clingo.symbol.Symbol]:
            facts = []
            for (r, c), v in self.board.sudoku.items():
                facts.append(clingo.Function("initial", [clingo.Number(r),clingo.Number(c),clingo.Number(v)]))
            return facts


if __name__ == "__main__":
    clingo_main(SudokuApp(), sys.argv[1:])

