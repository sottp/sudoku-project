#!/bin/python3

import argparse
import io
import sys
import unittest
from abc import ABC, abstractmethod
from typing import Optional

if sys.version_info < (3, 9):
    raise SystemExit("Sorry, this code need Python 3.9 or higher")


class Question(ABC):
    @abstractmethod
    def eval(self):
        pass

    @abstractmethod
    def score(self) -> int:
        pass

    @abstractmethod
    def max_score(self) -> int:
        pass

    def subquestions(self) -> dict[str, "Question"]:
        return {self.name: self}


class QuestionALL(Question):
    def __init__(self, name: str, questions: list[Question], display_name=None):
        self.name = name
        if display_name is None:
            self.display_name = name
        else:
            self.display_name = display_name
        self._questions = questions

    def eval(self):
        success = True
        failing_tests = []
        for question in self._questions:
            s, ft = question.eval()
            success = success & s
            failing_tests.extend(ft)
        sys.stdout.write(" " * 10)
        sys.stdout.write(f" {self.display_name:.<19}")
        sys.stdout.write(f" \t score: {self.score():3}/{self.max_score()}\n")
        return success, failing_tests

    def subquestions(self) -> dict[str, Question]:
        subquestions = {}
        for question in self._questions:
            subquestions.update(question.subquestions())
        subquestions.update({self.name: self})
        return subquestions

    def score(self) -> int:
        return sum(q.score() for q in self._questions)

    def max_score(self) -> int:
        return sum(q.max_score() for q in self._questions)


class QuestionUnitTestAll(Question):
    def __init__(self, name, tests: dict[str, Optional[list[str]]], max_points: int):
        self.name = name
        self.tests = tests
        self.max_points = max_points
        self.points = None

    def eval(self):
        sys.stdout.write(f"evaluating {self.name}...".ljust(25))
        success = True
        failing_tests = []
        for test in self.tests:
            test_out = io.StringIO()
            runner = unittest.TextTestRunner(test_out)
            itersuite = unittest.TestLoader().loadTestsFromName(test)
            test_result = runner.run(itersuite)
            if not test_result.wasSuccessful():
                success = False
                failing_tests.extend(test_result.failures)
                failing_tests.extend(test_result.errors)
        if success:
            self.points = self.max_points
        else:
            self.points = 0
        sys.stdout.write(f" done \t score: {self.points:3}/{self.max_points}\n")
        return success, failing_tests

    def score(self) -> int:
        if self.points is None:
            self.eval()
        return self.points

    def max_score(self) -> int:
        return self.max_points


question1a = QuestionUnitTestAll(
    name="question 1a",
    tests={
        "tests.test_sudoku1.TestSudokuUnsorted": None,
    },
    max_points=10,
)

question1b = QuestionUnitTestAll(
    name="question 1b",
    tests={
        "tests.test_sudoku1.TestSudokuSorted": None,
    },
    max_points=10,
)

question1 = QuestionALL(
    name="question 1",
    questions=[question1a, question1b],
)

question2 = QuestionUnitTestAll(
    name="question 2",
    tests={
        "tests.test_sudoku_model": None,
    },
    max_points=10,
)

question3 = QuestionUnitTestAll(
    name="question 3",
    tests={
        "tests.test_sudoku_str": None,
    },
    max_points=10,
)

question4 = QuestionUnitTestAll(
    name="question 4",
    tests={
        "tests.test_sudoku4": None,
    },
    max_points=30,
)

question5 = QuestionUnitTestAll(
    name="question 5",
    tests={
        "tests.test_sudoku_parsing": None,
    },
    max_points=10,
)

question6a = QuestionUnitTestAll(
    name="question 6a",
    tests={
        "tests.test_context": None,
    },
    max_points=10,
)

question6b = QuestionUnitTestAll(
    name="question 6b",
    tests={
        "tests.test_sudoku6": None,
    },
    max_points=10,
)

question6 = QuestionALL(
    name="question 6",
    questions=[question6a, question6b],
)

questionALL = QuestionALL(
    name="question ALL",
    questions=[question1, question2, question3, question4, question5, question6],
    display_name="All questions",
)


questions = questionALL.subquestions()


def dispatch_question(args):
    question_name = f"question {args.question}"
    if question_name in questions:
        return questions[question_name]
    else:
        raise Exception("Question not found", args.question)


def parse():
    parser = argparse.ArgumentParser(description="Test Grounder")
    question_choices = [q.removeprefix("question ") for q in questions.keys()]
    parser.add_argument(
        "--question",
        metavar="N",
        help="Question number.",
        required=False,
        default=None,
        choices=question_choices,
    )

    parser.add_argument(
        "--timeout",
        "-t",
        metavar="N",
        type=int,
        help="Time allocated to each instance.",
        required=False,
        default=180,
    )

    parser.add_argument(
        "--generate-solutions",
        metavar="<dir>",
        help="Path to a directory to write solutions. If does not exist, it will be created.",
        required=False,
        default=None,
    )
    args = parser.parse_args()

    if args.question is None:
        args.question = "ALL"

    return args


def main():
    try:
        args = parse()
        if args.question:
            question = dispatch_question(args)
            success, failing_tests = question.eval()
            if success:
                sys.stdout.write("SUCCESS\n")
                return 0
            else:
                sys.stdout.write("FAILURE\n")
                sys.stdout.write("The following tests failed:\n")
                for error in failing_tests:
                    sys.stdout.write(f"   {str(error[0].id())}\n")
                sys.stdout.write(
                    "\nYou can get more information by running the test directly using the command:\n"
                )
                sys.stdout.write("   python -m unittest <name-of-failing-test>\n")
                return 1

    except Exception as e:
        if len(e.args) >= 1:
            if e.args[0] == "Question not found":
                sys.stderr.write(f"ERROR: {e.args[0]} {e.args[1]}\n")
                return 1
        raise e


if __name__ == "__main__":
    sys.exit(main())
