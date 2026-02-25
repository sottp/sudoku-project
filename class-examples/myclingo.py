import sys, clingo


class ClingoApp(clingo.application.Application):

    def main(self, ctl, files):
        for f in files:
            ctl.load(f)
        if not files:
            ctl.load("-")
        ctl.ground()
        ctl.solve()


if __name__ == "__main__":
    clingo.application.clingo_main(ClingoApp())