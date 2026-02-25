#!/home/fandinno/miniconda3/envs/potassco/bin/python
import sys
from clingo.application import Application, clingo_main

class ClingoApp(Application):

    def print_model(self, model, printer) -> None:
        symbols = sorted(model.symbols(shown=True))
        print(" ".join(str(s) for s in symbols))
        sys.stdout.flush()

    def main(self, ctl, files):
        try:
            for f in files:
                ctl.load(f)
            if not files:
                ctl.load("-")
            ctl.ground([("base", [])])
        except RuntimeError as error:
            print("*** ERROR: (clingo):", error)
            sys.stdout.flush()
            return
        ctl.solve()

if __name__ == "__main__":
    clingo_main(ClingoApp())