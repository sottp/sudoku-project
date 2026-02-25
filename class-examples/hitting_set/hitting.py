from os import system
import sys, clingo
from typing import Callable, List
from clingo import Model


class Context:

    def __init__(self, files):
        self.__sets = set()
        for f in files:
            self.load(f)

    def load(self, file):
        f = open(file, 'r')
        lines = f.readlines()
        self.__sets.update(frozenset(l.split()) for l in lines)

    def set(self) -> List[clingo.Symbol]:
        return [ clingo.Number(i) for i in range(1, len(self.__sets)+1) ]

    def element(self) -> List[clingo.Symbol]:
        sets = zip(range(1,len(self.__sets)+1), self.__sets)
        return [clingo.Tuple_((clingo.Number(i), clingo.Function(e))) 
                    for (i, s) in sets for e in s]

class ClingoApp(clingo.application.Application):

    def print_model(self, model: Model, printer: Callable[[], None]) -> None:
        symbols = model.symbols(shown=True)
        symbols = [str(s.arguments[0]) for s in symbols]
        symbols.sort()
        sys.stdout.write('{}\n'.format(' '.join(symbols)))
        sys.stdout.flush()

    def main(self, ctl, files):
        ctl.load("hitting.lp")
        ctl.load("hitting_py.lp")
        context = Context(files)
        ctl.ground([("base", [])], context)
        ctl.solve()


if __name__ == "__main__":
    clingo.application.clingo_main(ClingoApp())