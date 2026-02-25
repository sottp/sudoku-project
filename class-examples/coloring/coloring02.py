#!/home/fandinno/miniconda3/envs/potassco/bin/python
import sys, clingo, graphviz

answer_file_name = 'colored_graph.gv'


class ClingoApp(clingo.application.Application):

    def print_model(self, model, printer):
        print("{}".format("   ".join(map(lambda s: str(s),sorted(model.symbols(shown=True))))))
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
        for f in files:
            ctl.load(f)
        if not files:
            ctl.load("-")
        ctl.configuration.solve.models = '1'
        ctl.ground()
        ctl.solve()

if __name__ == "__main__":
    clingo.application.clingo_main(ClingoApp())