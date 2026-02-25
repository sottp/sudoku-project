import sys
from clingo.application import Application, clingo_main


class SudokuApp(Application):
    def main(self, ctl, files):

        for f in files:
            ctl.load(f)

        if not files:
            ctl.load("-")

        ctl.ground([("base", [])])
        ctl.solve()

    def print_model(self, model, printer):
        atoms = sorted(model.symbols(shown=True), key=str)
        print(" ".join(str(a) for a in atoms))



if __name__ == "__main__":
    clingo_main(SudokuApp(), sys.argv[1:])
