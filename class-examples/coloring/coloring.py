#!/home/fandinno/miniconda3/envs/potassco/bin/python
import sys, clingo, graphviz
from typing import List

answer_file_name = 'colored_graph.gv'

class Context:

    def __init__(self):
        self.__colors = []
        self.__nodes  = []
        self.__edges  = []
        

    def load(self, files):
        if len(files) != 1:
            sys.stderr.write("Invalid input format: a single file should be provided\n")
            return False
        for f in files:
            if not self._load(f):
                return False
        return True

    def _load(self, file):
        f = open(file, 'r')
        lines = f.readlines()
        if len(lines) < 2:
            sys.stderr.write("Invalid input format: file should have at least 2 lines\n")
            return False
        line = lines[0].strip()    
        self.__colors = [ clingo.Function(color) for color in line.split() ]
        line = lines[1].strip()
        if len(line) > 0:
            self.__nodes  = [ clingo.Function(node) for node in line.split() ]
        lines = lines[2:]
        i = 0
        for line in lines:
            i += 1
            nodes  = line.strip().split()
            if len(line) == 0:
                continue
            if len(line) < 2:
                sys.stderr.write("Invalid input format: line {}\n".format(2+i))
                return False
            origin      = clingo.Function(nodes[0])
            destination = clingo.Function(nodes[1])
            edge = clingo.Tuple_((origin, destination))
            self.__edges.append(edge)
        return True

    def color(self) -> List[clingo.Symbol]:
        return self.__colors

    def node(self) -> List[clingo.Symbol]:
        return self.__nodes

    def edge(self) -> List[clingo.Symbol]:
        return self.__edges

class ClingoApp(clingo.application.Application):

    def print_model(self, model, printer):
        print("{}".format("   ".join(str(s) for s in sorted(model.symbols(shown=True)))))
        dot = graphviz.Digraph()
        for symbol in model.symbols(atoms=True):
            if symbol.name == 'assign':
                node_name  = str(symbol.arguments[0])
                node_color = str(symbol.arguments[1])
                dot.node(node_name, style='filled', fillcolor=node_color)
            if symbol.name == 'edge':
                dot.edge(str(symbol.arguments[0]), str(symbol.arguments[1]))

        dot.render(answer_file_name)
        print("\nAnswer saved at {}.pdf".format(answer_file_name))
        sys.stdout.flush()

    def main(self, ctl, files):
        ctl.load("coloring.lp")
        ctl.load("coloring_py.lp")
        ctl.configuration.solve.models = '1'
        context = Context()
        if context.load(files):
            ctl.ground(context=context)
            ctl.solve()

if __name__ == "__main__":
    clingo.application.clingo_main(ClingoApp())