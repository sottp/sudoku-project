from typing import Tuple
import clingo

class Sudoku:
    def __init__(self, sudoku: dict[Tuple[int, int], int]):
        self.sudoku = sudoku

    def __str__(self) -> str:
        # s = ""
        # YOUR CODE HERE
        lines = []

        for r in range(1, 10):
            row_vals = []
            for c in range(1, 10):
                v = self.sudoku.get((r, c), "-")
                row_vals.append(str(v))

            line = (
                    " ".join(row_vals[0:3]) + "  " +
                    " ".join(row_vals[3:6]) + "  " +
                    " ".join(row_vals[6:9])
            )
            lines.append(line)

            if r in (3, 6):
                lines.append("")

        return "\n".join(lines)
    #     return s

    @classmethod
    def from_str(cls, s: str) -> "Sudoku":
        sudoku = {}
        # YOUR CODE HERE

        rows = [line.strip() for line in s.splitlines() if line.strip()]

        r = 1
        for line in rows:
            tokens = line.split()
            if len(tokens) != 9:
                raise ValueError(f"Invalid row: {line}")

            for c, tok in enumerate(tokens, start=1):
                if tok != "-":
                    sudoku[(r, c)] = int(tok)
            r += 1

        return cls(sudoku)

    @classmethod
    def from_model(cls, model: clingo.solving.Model) -> "Sudoku":
        sudoku = {}
        # YOUR CODE HERE
        r,c,v = 0,0,0

        for atom in model.symbols(shown=True):
            if len(atom.arguments) == 3:
            # if atom.name == "cell" and len(atom.arguments) == 3:
                r = atom.arguments[0].number
                c = atom.arguments[1].number
                v = atom.arguments[2].number
            sudoku[(r, c)] = v

        return cls(sudoku)


