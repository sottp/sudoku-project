import sys
from clingo.application import Application, clingo_main

import sys
import shutil

def lpCombine():
    destination = "combine.lp"
    append_file =  "instances/lp/ex00.lp"

    if len(sys.argv) == 2:
        append_file = sys.argv[1]

    open(destination, "w").close()#wipe

    shutil.copyfile("sudoku.lp", destination)
    with open(append_file, "r") as f_in, open(destination, "a") as f_out:
        f_out.write(f_in.read())


class SudokuApp(Application):
    def main(self, ctl, files):
        lpCombine()

        ctl.load("combine.lp")

        for f in files:
            ctl.load(f)

        ctl.ground([("base", [])])
        ctl.solve()

    def print_model(self, model, printer):
        atoms = sorted(model.symbols(shown=True), key=str)
        print(" ".join(str(a) for a in atoms))

if __name__ == "__main__":
    clingo_main(SudokuApp(), sys.argv[1:])
