#!/home/fandinno/miniconda3/envs/potassco/bin/python
import sys, clingo


class ClingoApp(clingo.application.Application):

    def main(self, ctl, files):
        ctl.load("coloring.lp")
        ctl.load("graph01.lp")
        ctl.ground()
        ctl.solve()

if __name__ == "__main__":
    clingo.application.clingo_main(ClingoApp())