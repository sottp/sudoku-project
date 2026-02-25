import os
import subprocess
import sys
import unittest
import json


INSTANCES = "./instances/lp"
SOLUTIONS = "./solutions/q01"


def get_answer(command_line, sorted=True):
    output = subprocess.check_output(command_line, text=True, bufsize=1)
    output_lines = output.strip().splitlines()
    is_model = False
    for line in output_lines:
        if is_model:
            atoms = line.strip().split()
            if sorted:
                atoms.sort()
            return tuple(atoms)
        if line.startswith("Answer:"):
            is_model = True
        else:
            is_model = False


def get_answer_json(command_line, sorted=True):
    command_line.append("--outf=2")
    output = subprocess.check_output(command_line, text=True, bufsize=1)
    output_json = json.loads(output)
    answers = set()
    for v in output_json["Call"][0]["Witnesses"]:
        answer = v["Value"]
        if sorted:
            answer.sort()
        answers.add(tuple(answer))
    return answers


def get_solutions(file_name):
    solutions = set()
    with open(f"{SOLUTIONS}/{file_name}.json") as f:
        solution_json = json.load(f)
        for v in solution_json["Call"][0]["Witnesses"]:
            solution = v["Value"]
            solution.sort()
            solutions.add(tuple(solution))
    return solutions


class TestSudokuUnsorted(unittest.TestCase):
    def test_sudoku(self):
        for file in os.listdir(INSTANCES):
            file_name = os.path.splitext(os.path.basename(file))[0]
            output = get_answer([sys.executable, "-u", "sudoku1.py", f"{INSTANCES}/{file}"])
            solutions = get_solutions(file_name)
            self.assertIn(output, solutions)
            output = get_answer_json([sys.executable, "-u", "sudoku1.py", f"{INSTANCES}/{file}"])
            self.assertEqual(len(output), 1, file_name)
            for answer in output:
                self.assertIn(answer, solutions)


class TestSudokuSorted(unittest.TestCase):
    def test_sudoku(self):
        for file in os.listdir(INSTANCES):
            file_name = os.path.splitext(os.path.basename(file))[0]
            output = get_answer(
                [sys.executable, "-u", "sudoku1.py", f"{INSTANCES}/{file}"], sorted=False
            )
            solutions = get_solutions(file_name)
            self.assertIn(output, solutions)
