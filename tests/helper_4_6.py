import os
import subprocess
import sys
import unittest

def parse_answers(text):
    is_model = False
    answers = []
    answer = []
    for line in text.strip().splitlines():
        line = line.strip()
        if line == "":
            continue
        if is_model and len(answer) < 9:
            answer.append(line)
        if is_model and len(answer) >= 9:
            answers.append(tuple(answer))
            is_model = False
        if line.startswith("Answer:"):
            is_model = True
            answer = []
    return set(answers)

def get_answer(command_line, sorted=True):
    return parse_answers(subprocess.check_output(command_line, text=True, bufsize=1))


def get_solutions(solutions_path, file_name):
    with open(os.path.join(solutions_path, f"{file_name}.txt")) as f:
        solutions = parse_answers(f.read())
    return solutions


class TestSudoku46(unittest.TestCase):

    def helper_test_sudoku(self, instances_path, solutions_path, executable_path):
        for file in os.listdir(instances_path):
            file_name = os.path.splitext(os.path.basename(file))[0]
            output = get_answer([sys.executable, "-u", executable_path, os.path.join(instances_path, file)])
            solutions = get_solutions(solutions_path, file_name)
            self.assertEqual(len(output), 1, file_name)
            for answer in output:
                self.assertIn(answer, solutions, file_name)